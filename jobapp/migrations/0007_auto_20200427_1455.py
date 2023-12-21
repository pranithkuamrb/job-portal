import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_auto_20200427_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_des',
        ),
        migrations.AlterField(
            model_name='job',
            name='des',
            field=ckeditor.fields.RichTextField(blank=True, default=' '),
            preserve_default=False,
        ),
    ]
