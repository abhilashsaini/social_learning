# Generated by Django 2.2.6 on 2020-04-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_auto_20200413_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(default='2020-04-13 12:43:15.064115'),
        ),
        migrations.AlterField(
            model_name='video',
            name='creation_time',
            field=models.DateTimeField(default='2020-04-13 12:43:15.064115'),
        ),
    ]
