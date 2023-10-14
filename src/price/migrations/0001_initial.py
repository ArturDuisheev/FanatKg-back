# Generated by Django 4.2.6 on 2023-10-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано в: ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновленно в: ')),
                ('hour', models.CharField(max_length=255, verbose_name='hour')),
                ('price', models.IntegerField(verbose_name='price')),
                ('currency', models.CharField(max_length=6, verbose_name='currency')),
                ('to', models.CharField(blank=True, max_length=255, null=True, verbose_name='to')),
                ('from_hour', models.CharField(blank=True, max_length=255, null=True, verbose_name='from')),
            ],
            options={
                'verbose_name': 'Прайс',
                'verbose_name_plural': 'Прайсы',
            },
        ),
        migrations.CreateModel(
            name='HallList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано в: ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновленно в: ')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='street')),
                ('price_list', models.ManyToManyField(related_name='price_list', to='price.price', verbose_name='price')),
            ],
            options={
                'verbose_name': 'Список залов',
                'verbose_name_plural': 'Списки залов',
            },
        ),
    ]
