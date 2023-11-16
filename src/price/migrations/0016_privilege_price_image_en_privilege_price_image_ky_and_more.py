# Generated by Django 4.2.6 on 2023-11-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0015_rename_name_location_street_location_street_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privilege',
            name='price_image_en',
            field=models.ImageField(blank=True, null=True, upload_to='images/price_in_depth/', verbose_name='Изображение прайсов'),
        ),
        migrations.AddField(
            model_name='privilege',
            name='price_image_ky',
            field=models.ImageField(blank=True, null=True, upload_to='images/price_in_depth/', verbose_name='Изображение прайсов'),
        ),
        migrations.AddField(
            model_name='privilege',
            name='price_image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='images/price_in_depth/', verbose_name='Изображение прайсов'),
        ),
    ]