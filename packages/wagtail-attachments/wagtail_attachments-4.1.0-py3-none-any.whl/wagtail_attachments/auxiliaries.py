import collections
import copy

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.conf import settings
from django.core.files.storage import get_storage_class
from django.utils.functional import LazyObject, cached_property
from django.template.loader import render_to_string

from .models.mixins import AttachmentListener
from .apps import get_app_label

__all__ = ['gather_attachment_urls', 'concatenate_text_attachments', 'concatenate_binary_attachments']

APP_LABEL = get_app_label()


def gather_attachment_urls(attachable_class, role_identifier):

    urls = []

    for attachable in attachable_class.objects.all():
        attachments = attachable.attachments_for_role_identifier(role_identifier)

        for attachment in attachments:
            urls.append(attachment.file.url)

    return urls


def concatenate_text_attachments(attachable_class, role_identifier, delimiter, encoding='utf-8'):

    result = ''

    for attachable in attachable_class.objects.all():
        attachments = attachable.attachments_for_role_identifier(role_identifier)

        for attachment in attachments:
            result += attachment.read_text(encoding=encoding)
            result += delimiter

    return result


def concatenate_binary_attachments(attachable_class, role_identifier, delimiter):

    result = b''

    for attachable in attachable_class.objects.all():
        attachments = attachable.attachments_for_role_identifier(role_identifier)

        for attachment in attachments:
            result += attachment.read_bytes()
            result += delimiter

    return result


def aggregate_attachments(attachable_class, role_identifier, delimiter, file_name):

    aggregate = concatenate_text_attachments(attachable_class, role_identifier, delimiter)
    file = ContentFile(aggregate)
    saved_path = save_file(file_name, file)
    return saved_path


def save_file(local_path, content, storage=None):

    if storage is None:
        storage = default_storage

    available_path = storage.get_available_name(local_path)

    if local_path != available_path:
        storage.delete(local_path)

    saved_path = storage.save(local_path, content)
    return saved_path


class ConfiguredStorage(LazyObject):
    def _setup(self):
        storage_class = settings.WAGTAIL_ATTACHMENTS_SUPPORT_STORAGE
        self._wrapped = get_storage_class(storage_class)()


supportfiles_storage = ConfiguredStorage()


class InclusionState:

    @property
    def stylesheet_urls(self):
        return self.stylesheet_urls_dict.keys()

    @property
    def script_urls(self):
        return self.script_urls_dict.keys()

    def __init__(self):

        self.stylesheet_urls_dict = collections.OrderedDict()
        self.stylesheets = []

        self.script_urls_dict = collections.OrderedDict()
        self.scripts = []

    def add_definition(self, target, content):

        if target == 'stylesheet_urls':
            self.stylesheet_urls_dict[content] = None
        elif target == 'stylesheets':
            self.stylesheets.append(content)
        elif target == 'script_urls':
            self.script_urls_dict[content] = None
        elif target == 'stylesheets':
            self.scripts.append(content)


    def update_context(self, context):

        context['stylesheet_urls'] = self.stylesheet_urls
        context['stylesheets'] = self.stylesheets
        context['script_urls'] = self.script_urls
        context['scripts'] = self.scripts

    def __add__(self, other):

        result = copy.copy(self)

        result.stylesheet_urls_dict.update(other.stylesheet_urls_dict)
        result.stylesheets.extend(other.stylesheets)

        result.script_urls_dict.update(other.script_urls_dict)
        result.scripts.extend(other.scripts)

        return result


class InclusionContext:

    def __init__(self, handlers, template_name):
        self.handlers = list(handlers)
        self.update_counts = [-1] * len(self.handlers)
        self.template_name = template_name
        self.html_cache = {}

    def render(self, is_admin_page, container_element):

        state = InclusionState()

        for index, handler in enumerate(self.handlers):
            handler_state = handler.state_for(is_admin_page=is_admin_page, container_element=container_element)

            if handler_state:
                self.update_counts[index] = handler.update_count
                state += handler_state

        context = dict()
        context['is_admin_page'] = is_admin_page
        context['container_element'] = container_element

        state.update_context(context)

        result = render_to_string(self.template_name, context=context)

        by_container = self.html_cache.setdefault(container_element, {})
        by_container[is_admin_page] = result

        return result

    def is_cache_valid(self, is_admin_page, container_element):

        for index, handler in enumerate(self.handlers):
            handler_state = handler.state_for(is_admin_page=is_admin_page, container_element=container_element)

            if not handler_state:
                continue

            if handler.update_count > self.update_counts[index]:
                return False

        return True

    def html_for(self, is_admin_page, container_element):

        by_container = self.html_cache.get(container_element, None)
        result = by_container.get(is_admin_page, None) if by_container else None

        if result is None or not self.is_cache_valid(is_admin_page, container_element):
            result = self.render(is_admin_page, container_element)

        return result


class IncludeHandler(AttachmentListener):

    @property
    def target(self):

        target = None

        if self.attachment_role == 'css':
            if self.link_only:
                target = 'stylesheet_urls'
            else:
                target = 'stylesheets'
        elif self.attachment_role == 'js':
            if self.link_only:
                target = 'script_urls'
            else:
                target = 'scripts'

        return target

    def __init__(self, attachment_role, attachable_label, attachable_filters, link_only, container_element):
        super(IncludeHandler, self).__init__(attachment_role, attachable_label, attachable_filters)
        self.link_only = link_only
        self.container_element = container_element
        self.state = InclusionState()
        self.update_count = 0

    def state_for(self, *, is_admin_page, container_element, **kwargs):

        if container_element == self.container_element:

            if self.update_count == 0:
                self.update_state()

            return self.state

        return None

    def gather_attachments(self):
        attachables = self.attachable_model.objects.all().filter(**self.attachable_filters).values_list('id', flat=True)
        attachments = self.attachment_model.objects.all().filter(model__in=attachables, role__identifier=self.attachment_role)
        return attachments

    def update_files(self):
        return []

    def compute_state(self):

        state = InclusionState()
        target = self.target

        for file, url in self.update_files():

            if self.link_only:
                content = url
            else:
                file.seek(0)
                content = file.read().decode(encoding='utf-8')

            state.add_definition(target, content)

        return state

    def update_state(self):
        self.state = self.compute_state()
        self.update_count += 1

    def attachment_changed(self, attachment):
        self.update_state()


class IncludeIndividually(IncludeHandler):

    def __init__(self, attachment_role, attachable_label, container_element, link_only=True, attachable_filters=None):
        super(IncludeIndividually, self).__init__(
            attachment_role,
            attachable_label,
            attachable_filters,
            link_only,
            container_element)

    def update_files(self):

        attachments = self.gather_attachments()
        result = [(attachment.file, attachment.file.url) for attachment in attachments]
        return result


class IncludeConcatenation(IncludeHandler):

    @property
    def is_binary(self):
        return isinstance(self.delimiter, bytes)

    def __init__(self, attachment_role, attachable_label, container_element,
                 file_name, delimiter="\n", link_only=True, attachable_filters=None):
        super(IncludeConcatenation, self).__init__(
            attachment_role,
            attachable_label,
            attachable_filters,
            link_only,
            container_element)

        self.file_name = file_name
        self.delimiter = delimiter

    def update_files(self):

        attachments = self.gather_attachments()

        if self.is_binary:
            result = b''

            for attachment in attachments:
                result += attachment.read_bytes()
                result += self.delimiter

        else:
            result = ''

            for attachment in attachments:
                result += attachment.read_text()
                result += self.delimiter

        file = ContentFile(result)
        saved_name = save_file(self.file_name, file, supportfiles_storage)
        url = supportfiles_storage.url(saved_name)
        return [(file, url)]


def support_tag(*handlers, register, template_name=None, name=None):

    template_name = template_name if template_name else APP_LABEL + "/support_tag.html"

    def wrapper(f):

        context = InclusionContext(handlers, template_name)
        tag_name = name if name is not None else f.__name__

        def adapter(*args, **kwargs):
            return f(context, *args, **kwargs)

        d = register.simple_tag(takes_context=False, name=tag_name)
        adapter = d(adapter)

        return adapter

    return wrapper

"""
@support_tag(
    IncludeConcatenation("css", "aldine.layout", "head", "aldine/layouts.css"),
    IncludeConcatenation("js", "aldine.layout", "body", "aldine/layouts.js"),
    register=None,
)
def aldine_support(context, *, is_admin_tag, container_element):
    return context.html_for(is_admin_tag, container_element)
"""
