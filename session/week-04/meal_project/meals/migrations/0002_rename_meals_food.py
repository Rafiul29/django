# Generated by Django 4.2.13 on 2024-06-05 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meals',
            new_name='Food',
        ),
    ]
