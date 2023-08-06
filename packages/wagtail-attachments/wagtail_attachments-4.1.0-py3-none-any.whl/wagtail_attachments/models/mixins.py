import os
import re
import types

from django.apps import apps
from django.core.files.storage import default_storage
from django.utils.functional import cached_property
from django.db.models.signals import pre_delete, post_delete, post_save
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from .attachment_fields import AttachmentFile
from .attachment_roles import AttachmentRole
from ..apps import get_app_label

APP_LABEL = get_app_label()


ATTACHMENT_LISTENER_REGISTRY = {}


class AttachmentListener:

    @cached_property
    def attachable_model(self):
        return apps.get_model(self.attachable_label)

    @cached_property
    def attachment_label(self):
        return self.attachable_label + "Attachment"

    @cached_property
    def attachment_model(self):
        return apps.get_model(self.attachment_label)

    def __init__(self, attachment_role, attachable_label, attachable_filters):

        if attachable_filters is None:
            attachable_filters = {}

        self.attachment_role = attachment_role
        self.attachable_label = attachable_label
        self.attachable_filters = attachable_filters
        self.__register()

    def __register(self):

        listeners_by_attachable = ATTACHMENT_LISTENER_REGISTRY.setdefault(self.attachable_label, {})
        listeners = listeners_by_attachable.setdefault(self.attachment_role, [])
        listeners.append(self)

    def deregister(self):

        listeners_by_attachable = ATTACHMENT_LISTENER_REGISTRY.get(self.attachable_label, None)

        if listeners_by_attachable is None:
            return

        listeners = listeners_by_attachable.get(self.attachment_role, None)

        if listeners is None:
            return

        try:
            index = listeners.index(self)
            listeners.pop(index)
        except ValueError:
            pass

        if not listeners:
            listeners_by_attachable.pop(self.attachment_role)

        if not listeners_by_attachable:
            ATTACHMENT_LISTENER_REGISTRY.pop(self.attachment_model)

    @staticmethod
    def listeners_for(attachable_label, attachment_role):

        listeners_by_attachable = ATTACHMENT_LISTENER_REGISTRY.get(attachable_label, None)

        if not listeners_by_attachable:
            return None

        listeners = listeners_by_attachable.get(attachment_role, None)
        return listeners

    def attachment_changed(self, attachment):
        pass


class AttachableMixin:

    class Meta:
        abstract: True

    attachments = None

    @property
    def attachment_count(self):
        result = len(AttachmentRole.objects.all().filter(model=self)) # noqa
        return result

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_attachment_range(cls):
        return None, None

    @classmethod
    def get_attachment_file_class(cls, role):
        """
        Invoked by AttachmentField
        :return:
        """
        return AttachmentFile

    @classmethod
    def get_attachment_attributes(cls, role):
        """
        Invoked by AttachmentField
        :return:
        """
        return []

    def attachment_saved(self, attachment):
        pass

    def attachment_deleted(self, attachment):
        pass

    def attachments_for_role_identifier(self, role_identifier):
        role = AttachmentRole.objects.get(identifier=role_identifier)
        return self.attachments.filter(role__id=role.id) # noqa

    def attachments_by_role_identifier(self):

        result = types.SimpleNamespace()

        for role in AttachmentRole.objects.all():
            queryset = self.attachments.filter(role__identifier=role.identifier)
            setattr(result, role.identifier, queryset)

        return result


def handle_attachment_saved(attachable, attachment):

    listeners = AttachmentListener.listeners_for(attachable.__class__._meta.label_lower, attachment.role.identifier)

    if listeners:
        for listener in listeners:
            listener.attachment_changed(attachment)


def handle_attachment_deleted(attachable, attachment):

    listeners = AttachmentListener.listeners_for(attachable.__class__._meta.label_lower, attachment.role.identifier)

    if listeners:
        for listener in listeners:
            listener.attachment_changed(attachment)


CC_REGEXP = re.compile('([^A-Z_])([A-Z])')


def camel_case_to_snake_case(fragment):
    return CC_REGEXP.sub(r'\1_\2', fragment).lower()


class ClassProperty:

    def __init__(self, cls_get):
        self.cls_get = cls_get

    def __get__(self, instance, cls=None):

        if instance is not None:
            cls = instance.__class__

        if cls is None:
            return self

        return self.cls_get.__func__(cls)


class StorageMixin:

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_ = None

    @classmethod
    def get_storage_root(cls):

        if hasattr(cls._meta, 'verbose_name_plural'):
            default_root = "_".join(cls._meta.verbose_name_plural.split()).lower()
        elif hasattr(cls._meta, 'verbose_name'):
            default_root = "_".join((cls._meta.verbose_name + "s").split()).lower()
        else:
            default_root = camel_case_to_snake_case(cls.__name__)

        setting_name = cls._meta.app_label.upper() + "_" + default_root.upper() + "_STORAGE_ROOT"

        if hasattr(settings, setting_name):
            default_root = settings.setting_name

        return default_root

    storage_root = ClassProperty(cls_get=get_storage_root)

    @property
    def path(self):
        if self.path_ is None:
            self.path_ = self._build_path()

        return self.path_

    # noinspection PyMethodMayBeStatic
    def is_stored_locally(self):
        return False

    def _build_path(self):
        path = os.path.join(self.storage_root, '{:d}'.format(self.id)) # noqa
        return path

    @cached_property
    def local_attachments_path(self):
        return 'attachments/'

    @cached_property
    def attachments_path(self):
        return os.path.join(self.path, self.local_attachments_path)

    def delete_attachments(self):

        try:
            self.delete_storage_tree_at(default_storage, self.attachments_path)
        except NotImplementedError:
            pass

    @cached_property
    def local_content_path(self):
        return 'content/'

    @cached_property
    def content_path(self):
        return os.path.join(self.path, self.local_content_path)

    def content_url_for(self, name):
        return default_storage.url(os.path.join(self.content_path, name))

    def delete_contents(self):

        try:
            if self.created_at is not None:  # noqa
                self.delete_storage_tree_at(default_storage, self.content_path)
        except NotImplementedError:
            pass

    @staticmethod
    def delete_storage_tree_at(storage, path):

        try:
            root_directories, root_files = storage.listdir(path)
        except FileNotFoundError:
            return

        stack = [(root_directories, root_files, 0, path)]

        while stack:

            directories, files, index, root_path = stack[-1]  # noqa

            if index < len(directories):

                stack[-1] = directories, files, index + 1, root_path

                root_path = os.path.join(root_path, directories[index])

                try:
                    nested_directories, nested_files = storage.listdir(root_path)
                    stack.append((nested_directories, nested_files, 0, root_path))
                except FileNotFoundError:
                    pass

                continue

            for file in files:
                file_path = os.path.join(root_path, file)

                try:
                    storage.delete(file_path)
                except FileNotFoundError:
                    pass

            for directory in directories:
                directory_path = os.path.join(root_path, directory)
                storage.delete(directory_path)

            stack.pop()

        storage.delete(path)

    @staticmethod
    def will_be_deleted(instance, **kwargs):
        _ = instance.path
        pass

    @staticmethod
    def was_deleted(instance, **kwargs):

        try:
            instance.delete_storage_tree_at(default_storage, instance.path)
        except NotImplementedError:
            pass

        pass

    @classmethod
    def register_storage_signal_handlers(cls):

        """

        Call for each derived class in AppConfig.ready() !

        :return:
        """

        pre_delete.connect(cls.will_be_deleted, sender=cls)
        post_delete.connect(cls.was_deleted, sender=cls)


class SpecificMixin:

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.id: # noqa

            self.id = None

            if hasattr(self.__class__, 'content_type') and not self.content_type_id: # noqa

                self.content_type_id = ContentType.objects.get_for_model(self).id

    @property
    def cached_content_type(self):
        """
        .. versionadded:: 2.10

        Return this media_item's ``content_type`` value from the ``ContentType``
        model's cached manager, which will avoid a database query if the
        object is already in memory.
        """
        return ContentType.objects.get_for_id(
                self.content_type_id)  # noqa

    @cached_property
    def specific_class(self):
        """
        Return the class that this media item would be if instantiated in its
        most specific form.

        If the model class can no longer be found in the codebase, and the
        relevant ``ContentType`` has been removed by a database migration,
        the return value will be ``None``.

        If the model class can no longer be found in the codebase, but the
        relevant ``ContentType`` is still present in the database (usually a
        result of switching between git branches without running or reverting
        database migrations beforehand), the return value will be ``None``.
        """
        return self.cached_content_type.model_class()

    @cached_property
    def specific(self):
        """
        Returns this media_item in its most specific subclassed form with all field
        values fetched from the database. The result is cached in memory.
        """
        return self.get_specific()

    @cached_property
    def specific_deferred(self):
        """
        .. versionadded:: 2.12

        Returns this media_item in its most specific subclassed form without any
        additional field values being fetched from the database. The result
        is cached in memory.
        """
        return self.get_specific(deferred=True)

    def get_specific(self, deferred=False, copy_attrs=None):
        """
        .. versionadded:: 2.12

        Return this media_item in its most specific subclassed form.

        By default, a database query is made to fetch all field values for the
        specific object. If you only require access to custom methods or other
        non-field attributes on the specific object, you can use
        ``deferred=True`` to avoid this query. However, any attempts to access
        specific field values from the returned object will trigger additional
        database queries.

        If there are attribute values on this object that you wish to be copied
        over to the specific version (for example: evaluated relationship field
        values, annotations or cached properties), use `copy_attrs`` to pass an
        iterable of names of attributes you wish to be copied.

        If called on a media_item object that is already an instance of the most
        specific class (e.g. an ``EventPage``), the object will be returned
        as is, and no database queries or other operations will be triggered.

        If the media_item was originally created using a media_item type that has since
        been removed from the codebase, a generic ``Page`` object will be
        returned (without any custom field values or other functionality
        present on the original class). Usually, deleting these pages is the
        best course of action, but there is currently no safe way for Wagtail
        to do that at migration time.
        """

        model_class = self.specific_class

        if model_class is None:
            # The codebase and database are out of sync (e.g. the model exists
            # on a different git branch and migrations were not applied or
            # reverted before switching branches). So, the best we can do is
            # return the media_item in it's current form.
            return self

        if isinstance(self, model_class):
            # self is already the an instance of the most specific class
            return self

        if deferred:
            # Generate a tuple of values in the order expected by __init__(),
            # with missing values substituted with DEFERRED ()
            values = tuple(
                getattr(self, f.attname, self.pk if f.primary_key else DEFERRED)  # noqa
                for f in model_class._meta.concrete_fields
            )
            # Create object from known attribute values
            specific_obj = model_class(*values)
            specific_obj._state.adding = self._state.adding  # noqa
        else:
            # Fetch object from database
            specific_obj = model_class._default_manager.get(id=self.id)  # noqa

        # Copy additional attribute values
        for attr in copy_attrs or ():
            if attr in self.__dict__:
                setattr(specific_obj, attr, getattr(self, attr))

        return specific_obj

