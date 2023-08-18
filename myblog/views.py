from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import auth

# ListView.
class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    ordering = ['-id']

#DetailView
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'myblog/article_detail.html'

#CreateView
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/create_post.html'
    # fields = '__all__'

#category
class AddCategoryView(CreateView):
    model = Category 
    # form_class = EditForm
    template_name = 'myblog/Add_category.html'
    fields = '__all__'

#UpdateView
class UpdatePostView(UpdateView):
    model = Post 
    form_class = EditForm
    template_name = 'myblog/update_post.html'
    # fields = '__all__'

#DeleteView
class DeletePostView(DeleteView):
    model = Post 
    template_name = 'myblog/delete_post.html'
    fields = '__all__'
    success_url = '/'

# SignUp
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'You Sigunup Successfully.')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'myblog/user_signup.html',{'form':form})


#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You Logged In Successfylly.')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'myblog/user_login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#category page
def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'myblog/categories.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})
    