# Generated by Django 4.2.6 on 2023-10-13 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_remove_halllist_price_list_price_hall_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='hall_list',
            new_name='hall',
        ),
    ]
