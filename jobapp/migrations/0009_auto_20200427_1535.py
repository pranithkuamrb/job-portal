import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0008_job_company_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_des',
        ),
        migrations.RemoveField(
            model_name='job',
            name='des',
        ),
        migrations.AlterField(
            model_name='job',
            name='company_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
