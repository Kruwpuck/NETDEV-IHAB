# Generated by Django 5.0.6 on 2024-05-26 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioskop', '0003_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(default=2024),
        ),
    ]