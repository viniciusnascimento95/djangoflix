# Generated by Django 3.2.9 on 2021-11-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_videoproxy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
