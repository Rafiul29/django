# Generated by Django 4.2.11 on 2024-06-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/images/default.png', upload_to='.posts/images'),
        ),
    ]
