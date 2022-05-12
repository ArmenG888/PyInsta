# Generated by Django 4.0.4 on 2022-05-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_follower_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follower_users',
            field=models.ManyToManyField(blank=True, related_name='users_that_follow', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following_users',
            field=models.ManyToManyField(blank=True, related_name='users_following', to='users.profile'),
        ),
    ]
