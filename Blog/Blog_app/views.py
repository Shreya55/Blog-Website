from django.shortcuts import render,get_object_or_404 #404 pg would give an error if the pg user looks for doesent exists instead of blank blog pg
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) #class based views already present in django


# def home(request):
#     context = {'key1':Post.objects.all()}
#     return render(request, 'Blog_app/home.html',context)

def basic(request):
    return render(request, 'Blog_app/basic.html')

class PostListView(ListView):
    model = Post
    template_name = 'Blog_app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'key1'
    ordering = ['-Date']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'Blog_app/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'key1'
    ordering = ['-Date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(Author=user).order_by('-Date')
        #returns all the post of that user 


class PostDetailView(DetailView):#for individual post
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Title', 'Content']

    def form_valid(self, form): #to make sure that current loggedin user is the new post creator
        form.instance.Author = self.request.user
        return super().form_valid(form)

        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Title', 'Content']

    def form_valid(self, form): #to make current loggedin user as author of update post
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self): #to check if current loggedin user is author of update post
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #when post gets deleted then user is redirected to homepg

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

def about(request):
    return render(request, 'Blog_app/about.html',{'title':'About'})