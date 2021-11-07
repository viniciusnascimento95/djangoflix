# Generated by Django 3.2.9 on 2021-11-06 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20211102_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]