# this file is created bcoz we want a profile to be created for each new user registered 

from django.db.models.signals import post_save #this import signal is fired once we save our posts
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) #when sender(User) creates a post and it is saved(post_save we imported) and given to receiver(create_profile function) and performs the tasks of functions.
def create_profile(sender, instance, created, **kwargs): # this fn is called everytime a new user is created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #saving the profile of user 
    instance.profile.save()

#overall what signals does is just saving a profile being created everytime a new user is created .   
#also make sure to include it in apps.py of users_reg dir