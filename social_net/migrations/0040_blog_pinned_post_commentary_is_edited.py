# Generated by Django 5.1.4 on 2024-12-23 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0039_commentary_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pinned_post',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='social_net.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentary',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
    ]
