import re

from django.db import models as django_models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from wagtail.snippets.models import register_snippet


def validate_identifier(value):

    if re.search(r"(^[^A-Za-z0-9_]|\s)", value):

        raise ValidationError(
            _("Identifiers must start with a letter, a digit or underscore "
              "and cannot contain whitespace characters: {:}").format(value)
        )


@register_snippet
class AttachmentRole(django_models.Model):

    class Meta:
        verbose_name = 'Attachment Role'
        verbose_name_plural = 'Attachment Roles'
        constraints = [
            django_models.UniqueConstraint(fields=['identifier'], name='%(app_label)s_%(class)s_identifier_is_unique'),
            django_models.UniqueConstraint(fields=['name'], name='%(app_label)s_%(class)s_name_is_unique')
        ]

    identifier = django_models.CharField("Identifier", unique=True, max_length=255, blank=False, null=False,
                                         validators=[validate_identifier])

    name = django_models.CharField(
        verbose_name=_('name'),
        unique=True,
        max_length=255,
        blank=False,
        null=False,
        help_text=_("The attachment role name.")
    )

    def __str__(self):
        return "{}: {}".format(self.identifier, self.name)
