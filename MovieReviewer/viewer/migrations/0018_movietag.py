# Generated by Django 4.0.2 on 2022-06-13 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0017_remove_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.movie')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.tag')),
            ],
        ),
    ]
