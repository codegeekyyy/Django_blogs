from django.contrib import admin
from .models import Category, Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    list_editable = ('is_featured', 'status')
    list_filter = ('category', 'author', 'is_featured', 'status')
    search_fields = ('title', 'short_description', 'blog_body','category__name','author__username','status')
    ordering = ('-created_at',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
