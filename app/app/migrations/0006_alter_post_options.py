# Generated by Django 4.0.3 on 2022-04-12 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
    ]