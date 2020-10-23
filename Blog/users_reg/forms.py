from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # django already has UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): # adding email field in UserRegisterForm which has all attributes of UserCreationForm
    email = forms.EmailField()

    class Meta: # conf class which does all changes to model(User) and saves them
        model = User # model is set equal to User bcoz once user registers the form then the changes would be saved in User model also
        fields = ['username', 'email', 'password1', 'password2'] # fields is specified in order at which we want them to be shown in our form
        # like here first there will be a username then email then the two matching passwords


class UserUpdateForm(forms.ModelForm):# this form will allow user to update user email and username
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):# this form will allow the user to update his profile image
    
    class Meta: # includes models and fields we wanna work with
        model = Profile
        fields = ['image']