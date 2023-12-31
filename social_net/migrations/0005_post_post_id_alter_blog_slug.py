# Generated by Django 4.1.5 on 2023-09-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0004_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.PositiveIntegerField(default=0, verbose_name='ID поста'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
