# Generated by Django 5.0.7 on 2024-08-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='no album title', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='no song title', max_length=100),
        ),
    ]
