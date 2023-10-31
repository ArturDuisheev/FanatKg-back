# Generated by Django 4.2.6 on 2023-10-31 18:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='уникальный идентификатор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано в: ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновленно в: ')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('position_ru', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('address', models.CharField(max_length=100, verbose_name='Филиал')),
                ('address_ru', models.CharField(max_length=100, null=True, verbose_name='Филиал')),
                ('address_en', models.CharField(max_length=100, null=True, verbose_name='Филиал')),
                ('address_ky', models.CharField(max_length=100, null=True, verbose_name='Филиал')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('url_for_vacancy', models.URLField(verbose_name='Google_form')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
