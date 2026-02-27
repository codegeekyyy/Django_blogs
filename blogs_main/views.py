from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from assign.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .forms import RegistrationForm

def home(request):
    categories = Category.objects.all()
    feature_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-updated_at')
    post = Blog.objects.filter(is_featured=False, status="Published").order_by('-updated_at')
#fetch about us
    try:
        about = About.objects.first()
    except About.DoesNotExist:
        about = None
    context = {
            'categories': categories,
            'feature_posts': feature_posts,
            'post': post,
            'about': about,
    }
    return render(request, 'home.html', context)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


def login(request):
    # AuthenticationForm expects the request object first and, when POSTing,
    # the submitted data as a keyword argument.  this ensures it can perform
    # its own authentication check and add non‑field errors when credentials
    # are incorrect.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # form has already authenticated the user
            auth.login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')