# -*- coding: utf-8 -*-

import os
import hashlib
import inspect

from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.files.storage import default_storage
from django.db.models.signals import post_delete, post_save
from django.contrib.contenttypes.models import ContentType

from wagtail.models import Orderable

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel

from .attachment_fields import AttachmentField
from .attachment_roles import AttachmentRole
from .mixins import SpecificMixin, handle_attachment_saved, handle_attachment_deleted

__all__ = ['create_model_attachment_class']


def get_attachment_upload_path(self, filename):

    if not self.file.field.storage.exists(filename):
        filename = self.file.field.storage.get_valid_name(filename)

    # noinspection PyUnresolvedReferences
    filename = filename.encode('ascii', errors='replace').decode('ascii')

    # noinspection PyUnresolvedReferences
    path = os.path.join(self.model.attachments_path, filename)

    if len(path) >= 95:
        chars_to_trim = len(path) - 94
        prefix, extension = os.path.splitext(filename)
        filename = prefix[:-chars_to_trim] + extension
        # noinspection PyUnresolvedReferences
        path = os.path.join(self.model.attachments_path, filename)

    return path


def get_default_attachment_content_type():
    return ContentType.objects.get_for_model(ModelAttachment)


class ModelAttachment(SpecificMixin, Orderable):

    class Meta(Orderable.Meta):
        verbose_name = 'Model Attachment'
        verbose_name_plural = 'Model Attachments'

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name='model_attachments',
        on_delete=models.SET(get_default_attachment_content_type),
        editable=False
    )

    role = models.ForeignKey(AttachmentRole, related_name="attachments", on_delete=models.CASCADE, blank=False)
    file = AttachmentField(upload_to=get_attachment_upload_path, verbose_name=_('file'))

    file_hash = models.CharField(max_length=48, blank=True, editable=False)

    def _set_file_hash(self, file_contents):
        self.file_hash = hashlib.sha3_384(file_contents).hexdigest()

    def get_file_hash(self):
        if self.file_hash == '':
            with self.file.open() as f: # noqa
                self._set_file_hash(f.read())

            self.save(update_fields=['file_hash'])

        return self.file_hash

    def get_upload_path(self, filename):
        return get_attachment_upload_path(self, filename) # noqa

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    @property
    def file_extension(self):
        return os.path.splitext(self.filename)[1][1:]

    @property
    def filepath(self):
        return self.file.name if self.file else None

    panels = [
        FieldPanel('role'),
        FieldPanel('file')
    ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @staticmethod
    def was_saved(instance, **kwargs):
        handle_attachment_saved(instance.model, instance)
        instance.model.attachment_saved(instance)

    @staticmethod
    def was_deleted(instance, **kwargs):
        instance.file.delete(save=False)
        instance.model.attachment_deleted(instance)
        handle_attachment_deleted(instance.model, instance)

    @classmethod
    def register_signal_handlers(cls):

        for subclass in ModelAttachment.__subclasses__():
            post_save.connect(subclass.was_saved, sender=subclass)
            post_delete.connect(subclass.was_deleted, sender=subclass)

    def read_bytes(self):
        path = self.filepath

        if not path:
            return b''

        with default_storage.open(path) as file:
            return file.read()

    def read_text(self, encoding='utf-8'):
        path = self.filepath

        if not path:
            return ''

        with default_storage.open(path) as file:
            return file.read().decode(encoding=encoding)


def create_model_attachment_class(model_class):
    if not isinstance(model_class, ClusterableModel):
        RuntimeError('Model class for ModelAttachment must be derived from ClusterableModel')

    name = model_class.__name__ + 'Attachment'

    stack = inspect.stack()[1]
    module = inspect.getmodule(stack[0])

    class Meta:
        abstract = False

    attachment_class = type(name, (ModelAttachment,), {
        '__module__': module.__name__,
        'model': ParentalKey(model_class, related_name="attachments", on_delete=models.CASCADE, blank=False),
        'model_class': model_class,
        'Meta': Meta
    })

    return attachment_class
