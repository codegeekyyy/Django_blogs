from django.shortcuts import render
from blogs.models import Category, Blog
from assign.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

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
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)