# Generated by Django 4.2.11 on 2024-05-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='ra'),
        ),
    ]