from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class noteModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    note = models.TextField(blank=True)
    newUpdatedDate = models.DateTimeField(null=False)
    lastUpdatedDate = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
