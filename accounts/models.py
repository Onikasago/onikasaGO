from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    """拡張ユーザモデル"""

    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'CustomUser'
