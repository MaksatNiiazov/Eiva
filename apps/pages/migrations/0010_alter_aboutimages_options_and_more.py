# Generated by Django 5.0.7 on 2024-08-24 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_remove_aboutimages_page_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutimages',
            options={'verbose_name': 'Изображение партнера', 'verbose_name_plural': 'Изображения партнеров'},
        ),
        migrations.AlterModelOptions(
            name='contactinformation',
            options={'verbose_name': 'Контактная информация', 'verbose_name_plural': 'Контактная информация'},
        ),

    ]
