# Generated by Django 3.0.4 on 2020-04-11 20:05

from django.db import migrations, models
import videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20200411_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='notes',
            field=models.FileField(blank=True, null=True, upload_to=videos.models.file_upload_path),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(default='2020-04-12 01:35:56.698091'),
        ),
        migrations.AlterField(
            model_name='video',
            name='catagory',
            field=models.CharField(choices=[('cse', 'Computer Science'), ('phs', 'Philosphy'), ('phy', 'Physics'), ('mda', 'Media'), ('mth', 'Methametics'), ('art', 'Arts'), ('chy', 'Chemistry'), ('bio', 'Biology')], max_length=3),
        ),
        migrations.AlterField(
            model_name='video',
            name='creation_time',
            field=models.DateTimeField(default='2020-04-12 01:35:56.697049'),
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]