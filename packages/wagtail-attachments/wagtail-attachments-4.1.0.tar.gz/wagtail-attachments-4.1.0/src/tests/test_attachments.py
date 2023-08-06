
from django.test import TestCase

from wagtail_attachments.models.attachment_fields import ContentAttachmentFile


class AttachmentFileTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_file(self):

        text = "The quick brown fox jumped over the lazy dog."
        file = ContentAttachmentFile(text, name="hello.txt")

        with file.open() as handle:
            result = handle.read()

        self.assertEqual(text, result, "Content read from ContentAttachmentFile inconsistent.")
