from wagtail.admin.panels import InlinePanel


__all__ = ['AttachmentsPanel']


class AttachmentsPanel(InlinePanel):

    def __init__(self, **kwargs):

        if 'relation_name' not in kwargs:
            kwargs['relation_name'] = "attachments"

        if 'label' not in kwargs:
            kwargs['label'] = "Attachments"

        super().__init__(**kwargs)

    def on_model_bound(self):
        super(AttachmentsPanel, self).on_model_bound()

        attachment_range = self.model.get_attachment_range()

        self.min_num = attachment_range[0]
        self.max_num = attachment_range[1]
