from django.db import models
from django_facebook.models import FacebookCustomUser
from django.db.models.signals import post_save

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(FacebookCustomUser)

class Photo(models.Model):
	profile = models.ForeignKey(UserProfile)
	
	user_uploaded = models.BooleanField()
	fb_id = models.IntegerField()
	src = models.CharField(max_length=255)


