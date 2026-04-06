from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.db import models

from providers.models import Providers


# Create your models here.

class Notification(models.Model):
    CHANNEL_TYPE = (
        ('email', 'Email'),
        ('sms', 'SMS'),
    )
    user_id = models.CharField(max_length=100, blank=False, FOREIGN_KEY=True)
    provider_id = models.CharField(max_length=100, blank=False, FOREIGN_KEY=True)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    reference_id = models.CharField(max_length=100, blank=False, unique=True)
    channel_type = models.CharField(max_length=20, choices=CHANNEL_TYPE)


