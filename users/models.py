from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    insurance_number = models.CharField(max_length=255, blank=True, null=True)
    spouse = models.CharField(max_length=255, blank=True, null=True)
    children = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
