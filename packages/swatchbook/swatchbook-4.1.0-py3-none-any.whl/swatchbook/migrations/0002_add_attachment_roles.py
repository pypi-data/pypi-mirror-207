import os

from django.db import migrations, transaction
from django.utils import timezone
from django.conf import settings
from django.core.files.base import ContentFile


def define_default_fonts(apps, schema_editor):

    base_path = os.path.dirname(getattr(settings, 'BASE_DIR', None))
    fonts_path = os.path.join(base_path, "fonts")

    # noinspection PyPep8Naming
    AttachmentRole = apps.get_model('wagtail_attachments', 'AttachmentRole')

    with transaction.atomic():

        woff_role = AttachmentRole()
        woff_role.identifier = 'woff'
        woff_role.name = 'Web Open Font Format'
        woff_role.save()

        woff2_role = AttachmentRole()
        woff2_role.identifier = 'woff2'
        woff2_role.name = 'Web Open Font Format 2'
        woff2_role.save()


class Migration(migrations.Migration):

    dependencies = [
        ('swatchbook', '0001_initial'),
        ('wagtail_attachments', '0002_add_attachment_roles'),
    ]

    operations = [
        migrations.RunPython(define_default_fonts),
    ]