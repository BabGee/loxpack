# Generated by Django 3.0.2 on 2020-01-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='stats',
            new_name='name',
        ),
    ]