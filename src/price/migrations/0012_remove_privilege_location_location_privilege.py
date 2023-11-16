# Generated by Django 4.2.6 on 2023-11-07 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0011_location_delete_price_privilege_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privilege',
            name='location',
        ),
        migrations.AddField(
            model_name='location',
            name='privilege',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='privilege_location', to='price.privilege', verbose_name='Описание прайса'),
            preserve_default=False,
        ),
    ]