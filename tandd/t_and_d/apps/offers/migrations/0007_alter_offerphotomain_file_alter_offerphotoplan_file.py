# Generated by Django 4.2 on 2023-04-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_alter_offerphoto_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerphotomain',
            name='file',
            field=models.ImageField(upload_to='offer_photo_main', verbose_name='Файл с фото'),
        ),
        migrations.AlterField(
            model_name='offerphotoplan',
            name='file',
            field=models.ImageField(upload_to='offer_photo_plan', verbose_name='Файл с фото'),
        ),
    ]