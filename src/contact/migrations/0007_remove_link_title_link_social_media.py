# Generated by Django 4.2.6 on 2023-11-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_address_remove_contact_phones_remove_contact_streets_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='title',
        ),
        migrations.AddField(
            model_name='link',
            name='social_media',
            field=models.CharField(choices=[('Инстаграм', 'Инстаграм'), ('ТикТок', 'ТикТок'), ('Вотцап', 'Вотцап'), ('Телеграм', 'Телеграм')], default='Телеграм', max_length=17, verbose_name='Соц.Сети'),
        ),
    ]