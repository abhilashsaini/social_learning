# Generated by Django 3.0 on 2020-04-13 15:13

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('institute', models.CharField(max_length=50)),
                ('image', models.FileField(default='profile_img/user.png', null=True, upload_to=account.models.get_image_name)),
                ('interests', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='profile_img/user.png', null=True, upload_to=account.models.get_image_name1)),
                ('institute', models.CharField(max_length=50)),
                ('qualifications', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('work_experience', models.TextField(blank=True, null=True)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
