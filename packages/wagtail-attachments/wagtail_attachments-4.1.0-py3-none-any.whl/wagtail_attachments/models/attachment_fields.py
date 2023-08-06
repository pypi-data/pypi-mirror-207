# -*- coding: utf-8 -*-
import django.core.checks

from django import forms
from django.core import checks
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import signals
from django.db.models.fields.files import FileDescriptor, FieldFile as DjangoFieldFile
from django.utils.translation import gettext_lazy as _
from django.core.files.base import File, ContentFile

from modelcluster.models import ClusterableModel

__all__ = ['AttachmentFile', 'AttachmentDescriptor', 'AttachmentField', 'ContentAttachmentFile']


class AttachmentFile(File):

    """
    An attachment file provides a get_attributes() method to retrieve a dictionary of attributes
    retrieved from the underlying file. In order to load attributes from the file a subclass only has to
    override the load_attributes_from_file() method.
    """

    def get_attributes(self):

        if not hasattr(self, 'attributes_cache_'):
            close = self.closed

            self.open()
            setattr(self, 'attributes_cache_', self.load_attributes_from_file(close=close))

        return getattr(self, 'attributes_cache_')

    def load_attributes_from_file(self, close):

        result = {}

        if close:
            self.close()

        return result


class ContentAttachmentFile(ContentFile, AttachmentFile):
    pass


class AttachmentFieldFile(AttachmentFile, DjangoFieldFile):

    def save(self, name, content, save=True):
        generated_name = self.field.generate_filename(self.instance, name)
        provisional_name = self.storage.get_available_name(generated_name, max_length=self.field.max_length)

        if provisional_name != generated_name and self.storage.exists(generated_name):
            self.storage.delete(generated_name)

        super().save(name, content, save)

    def delete(self, save=True):
        # Clear the attributes cache

        if hasattr(self, 'attributes_cache_'):
            del self.attributes_cache_

        super().delete(save)


class AttachmentDescriptor(FileDescriptor):

    def __set__(self, instance, value):
        previous_file = instance.__dict__.get(self.field.name)
        super().__set__(instance, value)

        # To prevent recalculating image dimensions when we are instantiating
        # an object from the database (bug #11084), only update dimensions if
        # the field had a value before this assignment.  Since the default
        # value for FileField subclasses is an instance of field.attr_class,
        # previous_file will only be None when we are called from
        # Model.__init__().  The AttachmentField.updated_instance_attributes method
        # hooked up to the post_init signal handles the Model.__init__() cases.
        # Assignment happening outside of Model.__init__() will trigger the
        # update right here.

        if previous_file is not None:
            self.field.updated_instance_attributes(instance, force=True)


FIELD_FILE_CLASSES = {}


def build_field_file_class(file_class):

    if not issubclass(file_class, AttachmentFile):
        raise RuntimeError('Provided file class for attachment field must be a subclass of AttachmentFile')

    if file_class in FIELD_FILE_CLASSES:
        return FIELD_FILE_CLASSES[file_class]

    def delete(self, save=True):

        # Clear the attributes cache

        if hasattr(self, 'attributes_cache_'):
            del self.attributes_cache_

        DjangoFieldFile.delete(self, save)

    name = file_class.__name__ + 'Wrapper'
    field_file_class = type(name, (file_class, DjangoFieldFile,), {'delete': delete})
    FIELD_FILE_CLASSES[file_class] = field_file_class
    return field_file_class


class AttachmentField(models.FileField):

    """
    A model field that holds an attachment file and updates an optional list of model fields
    from attributes of the attachment file after model initialisation or when attname of the
    model instance is assigned.
    """

    # Used by descriptor_class to wrap the instance attribute value:
    # Any value returned by the descriptor_class will be of this class.
    # file_class = AttachmentFile

    descriptor_class = AttachmentDescriptor
    description = _("Attachment")

    def __init__(self, verbose_name=None, name=None, **kwargs):

        kwargs.setdefault('max_length', 255)
        super().__init__(verbose_name, name, **kwargs)

    def save_form_data(self, instance, data):

        if data is not None and not data:
            # False-ish value that is not None means clear file
            file = getattr(instance, self.attname)
            file.delete(save=False)

        super().save_form_data(instance, data)

    def has_role(self, instance):

        if not instance:
            return False

        try:
            value = instance.role
        except ObjectDoesNotExist:
            return False

        return value is not None

    # noinspection PyMethodMayBeStatic
    def get_model_class(self, instance):

        # noinspection PyPep8Naming
        result = ClusterableModel
        instance_class = instance.specific_class

        if hasattr(instance_class, 'model_class') and instance_class.model_class:
            # noinspection PyPep8Naming
            result = instance_class.model_class

        return result

    # noinspection PyMethodMayBeStatic
    def attr_class(self, instance, field, name):

        # noinspection PyPep8Naming
        ModelClass = self.get_model_class(instance)

        file_class = ModelClass.get_attachment_file_class(instance.role) if self.has_role(instance) else AttachmentFile
        attr_class_ = build_field_file_class(file_class)

        return attr_class_(instance, field, name)

    # noinspection PyMethodMayBeStatic
    def get_attribute_fields(self, instance):

        if not self.has_role(instance):
            return []

        # noinspection PyPep8Naming
        ModelClass = self.get_model_class(instance)

        result = list(ModelClass.get_attachment_attributes(instance.role))
        return result

    def pre_save(self, model_instance, add):

        file = super().pre_save(model_instance, add)
        return file

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self.check_attachment_requirements(),
        ]

    # noinspection PyMethodMayBeStatic
    def check_attachment_requirements(self):
        """ Return a list of django.core.checks.Error(s) if requirements are not met. """
        return []

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        # if self.attribute_fields:
        #    args.insert(0, list(self.attribute_fields))

        return name, path, args, kwargs

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)

        # Attach updated_instance_attributes so that attribute fields declared
        # after their corresponding attachment field don't stay cleared by
        # Model.__init__, see bug #11196.

        # Only run post-initialization attribute update on non-abstract models
        if not cls._meta.abstract:
            signals.post_init.connect(self.updated_instance_attributes, sender=cls)

    # noinspection PyMethodMayBeStatic
    def instance_has_missing_attribute_values(self, instance, attribute_fields):

        for identifier in attribute_fields:

            if not getattr(instance, identifier):
                return True

        return False

    # noinspection PyUnusedLocals
    def updated_instance_attributes(self, instance, force=False, *args, **kwargs):

        """
        Update attribute fields on instance, if defined.

        This method is hooked up to model's post_init signal to update
        attributes after instantiating a model instance.  However, attributes
        won't be updated if the attributes fields are already populated.  This
        avoids unnecessary recalculation when loading an object from the
        database.

        Attributes can be forced to update with force=True, which is how
        AttachmentFileDescriptor.__set__ calls this method.
        """

        # Nothing to update if no attribute fields were specified or if
        # the field is deferred.

        attribute_fields = self.get_attribute_fields(instance)

        if not attribute_fields or self.attname not in instance.__dict__:
            return

        # Because attname on instance is implemented by a AttachmentFileDescriptor,
        # the returned value will always be a attr_class (AttachmentFieldFile) instance.
        file = getattr(instance, self.attname)

        if not force:

            if not file:
                # Nothing to update if we have no file and not being forced to update.
                return

            if not self.instance_has_missing_attribute_values(instance, attribute_fields):
                # Nothing to update if instance is not missing attribute values and not being forced to update.
                return

        # Copy all attribute values from the file to the instance

        for identifier in attribute_fields:

            if file:
                value = getattr(file, identifier)
            else:
                value = None

            setattr(instance, identifier, value)

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': forms.FileField,
            **kwargs,
        })
