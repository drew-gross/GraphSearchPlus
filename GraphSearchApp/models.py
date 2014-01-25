from django.db import models
from django_facebook.models import FacebookCustomUser
from django.db.models.signals import post_save

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(FacebookCustomUser)

    TURK_STATUS_CHOICES = (
    		('N', "New"),
    		('P', "Pending"),
    		('C', "Complete")
    	)

    turk_status = models.CharField(max_length=1,
                                      choices=TURK_STATUS_CHOICES,
                                      default='N')

class Photo(models.Model):
	profile = models.ForeignKey(UserProfile)
	
	user_uploaded = models.BooleanField(default=False)
	fb_id = models.IntegerField()
	src = models.CharField(max_length=255)
	turked = models.BooleanField(default=False)
	flagged = models.BooleanField(default=False)
	removed = models.BooleanField(default=False)


