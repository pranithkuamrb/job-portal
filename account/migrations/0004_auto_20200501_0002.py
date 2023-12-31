from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200430_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('none', 'None'), ('employer', 'Employer'), ('employee', 'Employee')], default='none', max_length=10),
        ),
    ]
