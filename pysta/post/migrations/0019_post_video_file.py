# Generated by Django 4.0.4 on 2022-05-27 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_remove_post_image_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_file',
            field=models.BooleanField(default=False),
        ),
    ]