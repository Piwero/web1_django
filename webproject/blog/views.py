from django.shortcuts import render
from .models import Post, Category

# Create your views here.


def blog(request):
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {"posts": posts})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {"category": category, "posts": posts})
