import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_auto_20200427_1537'),
    ]

    operations = [
        migrations.AddField(
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
