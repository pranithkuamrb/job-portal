import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_auto_20200427_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_des',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='des',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
