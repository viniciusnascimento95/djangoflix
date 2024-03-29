# Generated by Django 3.2.9 on 2021-11-07 00:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_publish_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 7, 0, 54, 31, 663480, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
