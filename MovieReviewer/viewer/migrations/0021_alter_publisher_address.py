# Generated by Django 4.0.2 on 2022-06-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0020_address_alter_actor_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.address'),
        ),
    ]