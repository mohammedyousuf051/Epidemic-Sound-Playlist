# Generated by Django 3.2.12 on 2022-02-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_playlist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='all_tracks',
            field=models.TextField(default=[]),
        ),
    ]