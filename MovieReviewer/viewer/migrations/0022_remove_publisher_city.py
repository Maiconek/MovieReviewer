# Generated by Django 4.0.2 on 2022-06-15 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0021_alter_publisher_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='city',
        ),
    ]