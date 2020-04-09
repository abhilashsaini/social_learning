# Generated by Django 3.0.4 on 2020-04-09 14:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0003_auto_20200409_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 20, 26, 1, 783984)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('creation_time', models.DateTimeField(default=datetime.datetime(2020, 4, 9, 20, 26, 1, 784987))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
            ],
        ),
    ]
