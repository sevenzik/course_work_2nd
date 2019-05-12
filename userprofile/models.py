from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    lastNumberOfQuestions = models.BigIntegerField(default=0)
    last_theme = models.CharField(max_length=50, default="")
    test_started = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
