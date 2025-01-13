# Generated by Django 5.1.4 on 2025-01-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_userprofile_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar_small',
            field=models.ImageField(default='icy.jpg', upload_to='users_avatars/small/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='icy.jpg', upload_to='users_avatars/original/'),
        ),
    ]
