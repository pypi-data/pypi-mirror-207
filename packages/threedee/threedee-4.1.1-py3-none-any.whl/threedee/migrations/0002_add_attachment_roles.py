from django.db import migrations, transaction


def define_default_attachment_roles(apps, schema_editor):

    # noinspection PyPep8Naming
    AttachmentRole = apps.get_model('wagtail_attachments', 'AttachmentRole')

    with transaction.atomic():

        paraview_role = AttachmentRole()
        paraview_role.identifier = 'paraview_html'
        paraview_role.name = 'Paraview WebGL HTML'
        paraview_role.save()


class Migration(migrations.Migration):

    dependencies = [
        ('threedee', '0001_initial'),
        ('wagtail_attachments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(define_default_attachment_roles),
    ]