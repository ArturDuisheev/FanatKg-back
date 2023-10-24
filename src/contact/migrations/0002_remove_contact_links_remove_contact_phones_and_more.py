# Generated by Django 4.2.6 on 2023-10-24 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
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
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contact_links', to='contact.link', verbose_name='Links'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phones',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contact_phone', to='contact.phone', verbose_name='Phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='streets',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contact_street', to='contact.street', verbose_name='Street'),
            preserve_default=False,
        ),
    ]
