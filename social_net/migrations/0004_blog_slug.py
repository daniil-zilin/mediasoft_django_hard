# Generated by Django 4.1.5 on 2023-09-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0003_remove_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
