# Generated by Django 4.0.3 on 2022-04-07 10:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 7, 10, 7, 2, 782113, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
