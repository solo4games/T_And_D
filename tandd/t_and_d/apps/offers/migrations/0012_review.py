# Generated by Django 4.2 on 2023-05-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0011_alter_offer_deadline_alter_offer_house_area_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Аноним', max_length=255, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
