# Generated by Django 3.0.2 on 2020-01-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_property_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='property_pics'),
        ),
    ]