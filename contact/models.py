from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=15, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)