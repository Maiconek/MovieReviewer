# Generated by Django 4.0.2 on 2022-05-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0011_alter_movie_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
