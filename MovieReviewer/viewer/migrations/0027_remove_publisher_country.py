# Generated by Django 4.0.2 on 2022-06-15 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0026_alter_publisher_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='country',
        ),
    ]