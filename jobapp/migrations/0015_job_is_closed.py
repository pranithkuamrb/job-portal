from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0014_job_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
