from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0013_bookmarkjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
