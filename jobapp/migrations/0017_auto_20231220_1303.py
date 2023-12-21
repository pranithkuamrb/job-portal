from django.db import migrations
from django.db import migrations, models
import django.db.models.deletion

def add_category_data(apps, schema_editor):
    Category = apps.get_model('jobapp', 'Category')
    # Delete all existing categories
    Category.objects.all().delete()
    # Add sample category data
    categories = ['IT', 'Legal', 'Accounting']
    for category_name in categories:
        Category.objects.create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),  # Replace with your previous migration file
    ]

    operations = [
        migrations.RunPython(add_category_data),
    ]
