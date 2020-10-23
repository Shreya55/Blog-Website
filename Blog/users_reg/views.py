from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #django already provides this form
from django.contrib.auth.decorators import login_required #used in below decorator
from django.contrib import messages # messages is imported to display flash messages which are dispalyed once and then dissappear once the user clicks some button or refreshes the pg
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #form is a variable which stores all data we get from register pg through POST mthd(here email,username,password)
        if form.is_valid():
            form.save() #saves the data of the form which the user filled and performs next steps
            username = form.cleaned_data.get('username') # this variable stores the username from the register form he filled 
            messages.info(request,f'Account is created for {username}!')  
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users_reg/register.html', {'form':form})

# this fn is getting all data from UserRegisterForm and storing the username if the form is valid(credentials filled are
# correct) and then displaying a flash message(through messages we imported) on the home page (by redirecting to '/blog-
# home')




@login_required
# this decorator is used which tells that in order to view the profile ,the user must be logged in and decorators add 
# functionality so this decorator has added functionality to profile pg bcoz if the user isn't looged in then there will
# be a blank pg without showing any posts (bcoz posts would be visisble if user is logged in)

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance= request.user)
        #current user info(username,email) with its data from POST method is now displayed on user profile
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile) 
        # current user profile info, request.FILES gets all file data associated with img
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request,f'Your account has been updated successfully!')
            return redirect('profile') 
            # after updating user profile ,redirect him to his profile page with the successful flash message shown
    
    else: 
    # if user profile data is not recieved ie email and username fields are empty then create an instance of user and
    # his profile and render it in hi=s profile.html pg    
        u_form = UserUpdateForm(instance= request.user) 
        p_form = ProfileUpdateForm(instance= request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users_reg/profile.html', context)