from django.db import migrations, transaction


def define_default_attachment_roles(apps, schema_editor):

    # noinspection PyPep8Naming
    AttachmentRole = apps.get_model('wagtail_attachments', 'AttachmentRole')

    with transaction.atomic():
        css_role = AttachmentRole()
        css_role.identifier = 'css'
        css_role.name = 'Cascading Stylesheet'
        css_role.save()

        template_role = AttachmentRole()
        template_role.identifier = 'html'
        template_role.name = 'HTML Template'
        template_role.save()

        js_role = AttachmentRole()
        js_role.identifier = 'js'
        js_role.name = 'JavaScript'
        js_role.save()

        image_role = AttachmentRole()
        image_role.identifier = 'image'
        image_role.name = 'Image'
        image_role.save()

        svg_role = AttachmentRole()
        svg_role.identifier = 'svg'
        svg_role.name = 'Scalable Vector Graphics'
        svg_role.save()

        video_role = AttachmentRole()
        video_role.identifier = 'video'
        video_role.name = 'Video'
        video_role.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_attachments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(define_default_attachment_roles),
    ]