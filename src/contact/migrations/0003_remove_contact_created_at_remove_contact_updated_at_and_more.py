# Generated by Django 4.2.6 on 2023-10-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_links_remove_contact_phones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='links',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phones',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='streets',
        ),
        migrations.AddField(
            model_name='contact',
            name='links',
            field=models.ManyToManyField(related_name='contact_links', to='contact.link', verbose_name='Links'),
        ),
        migrations.AddField(
            model_name='contact',
            name='phones',
            field=models.ManyToManyField(related_name='contact_phones', to='contact.phone', verbose_name='Phones'),
        ),
        migrations.AddField(
            model_name='contact',
            name='streets',
            field=models.ManyToManyField(related_name='contact_streets', to='contact.street', verbose_name='Streets'),
        ),
    ]
