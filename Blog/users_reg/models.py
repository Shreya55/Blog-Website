from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #OneToOneField is making a one to one relationship with Profile class we are creating with the User model
    #on_delete tells that what we want to do with the pofile if the User is deleted
    #CASCADE - it deletes the profile if the user is deleted but doesent deletes the user if the profile is deleted

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # upload_to paramater does nothing but makes a profile_pics named directory (as we did upload_to = 'profile_pics')
    # and within that directory , all out profile images would be uploaded

    def __str__(self): #displays Profile object nicely
        return f'{self.user.username} Profile'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)


    # def save(self, *args, **kwargs): #save is a parent method which saves the work and is built-in in django 
    #     super().save(self, *args, **kwargs) #we are overwriting the save method of parent class through super()

        img = Image.open(self.image.path)#opens the current image of user profile

        if img.height > 300 or img.width > 300:#if the user profile image is very big then resize it to 300px and save it
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)