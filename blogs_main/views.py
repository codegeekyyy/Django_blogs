from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    categories = Category.objects.all()
    feature_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-updated_at')
    post = Blog.objects.filter(is_featured=False, status="Published").order_by('-updated_at')
    context = {
            'categories': categories,
            'feature_posts': feature_posts,
            'post': post,
    }
    return render(request, 'home.html', context)