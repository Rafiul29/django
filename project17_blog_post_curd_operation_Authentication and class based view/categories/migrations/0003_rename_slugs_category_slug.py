# Generated by Django 4.2.11 on 2024-06-04 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_slugs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slugs',
            new_name='slug',
        ),
    ]
