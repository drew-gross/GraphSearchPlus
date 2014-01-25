from django.db import models
from django_facebook.models import FacebookCustomUser
from django.db.models.signals import post_save

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(FacebookCustomUser)

