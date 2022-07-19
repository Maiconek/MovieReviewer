# Generated by Django 4.0.2 on 2022-05-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
