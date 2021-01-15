from django.db import models # to use the functionality of models in our db
from django.utils import timezone #for Date column in db
from django.contrib.auth.models import User # django already has User in admin page once you create a superuser
from django.urls import reverse #to redirect the user to post detail pg when post detail form is updated  


class Post(models.Model):
    Title = models.CharField(max_length = 100)
    Content = models.TextField() # textfield can be of any length so not specified in brackets
    Author = models.ForeignKey(User, on_delete = models.CASCADE) #cascade is used bcoz if user gets deleted then its post will also be deleted
    Date = models.DateTimeField(default= timezone.now)

# now the db containing Post model(class) gets created and the fields of this model can be viewed in migrations.py/0001_initial.py

    def __str__(self):
        return self.Title

    def get_absolute_url(self): #It tells the django where to go when new post is created.
        return reverse('post-detail', kwargs={'pk': self.pk})