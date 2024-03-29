from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    subscriptions = models.ManyToManyField('social_net.Blog', related_name="subscribers", blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
