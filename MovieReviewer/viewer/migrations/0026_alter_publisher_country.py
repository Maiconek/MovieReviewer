# Generated by Django 4.0.2 on 2022-06-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0025_alter_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
