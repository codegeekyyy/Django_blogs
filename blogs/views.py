from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    # fetch the posts that belong to the category with the id category_id
    posts = Blog.objects.filter(status="Published", category_id=category_id).order_by('-created_at')
    # category = get_object_or_404(Category, id=category_id)
      # use try-except when you want to show a custom page or redirect to another page
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     # redirect to home page
    #     return render(request, 'home.html')
    category =  get_object_or_404(Category, id=category_id)
    # use get_object_or_404 when you want to show 404 error page if the category does not exist
  
    context = {
        'posts': posts,
        'category': category,
        'categories': Category.objects.all(),
    }
    return render(request, 'posts_by_category.html', context)


def post_detail(request, slug):
  single_blog = get_object_or_404(Blog, slug=slug, status="Published")
  context = {
    'single_blog': single_blog,
    'categories': Category.objects.all(),
  }
  return render(request, 'post_detail.html', context)



def search(request):
  keyword = request.GET.get('keyword')
  posts = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published").order_by('-created_at')
  context = {
    'posts': posts,
    'keyword': keyword,
    'categories': Category.objects.all(),
  }
  return render(request, 'search.html', context)