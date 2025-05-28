from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blog, Category
from .forms import CommentForm
from util.views import group_queryset  # Agar bu sizda bo'lmasa, olib tashlang

def home(request):
    header = Blog.objects.order_by('-id')[:3]
    # recent = Category.objects.filter(name__in=['Politics', 'Technology'])

    bussines = Category.custom.get_category("Business")
    sports = Category.custom.get_category("Sports")
    gadgets = Category.custom.get_category("Gadgets and Technology")
    life_style = Category.custom.get_category("Life style")
    travels = Category.custom.get_category("Travels")

    blogs = Blog.objects.all()

    gadget_blogs = Blog.objects.filter(category=gadgets).order_by('-id')
    gadget_paginator = Paginator(gadget_blogs, 8)
    page_number = request.GET.get("page", 1)
    gadgets_by_page = gadget_paginator.get_page(page_number)

    recent_new = Blog.objects.all()

    context = {
        "banner": header,
        "recent_new": recent_new,
        "blogs": group_queryset(2, blogs),
        "bussines": bussines,
        "sports": sports,
        "gadgets": gadgets,
        "gadgets_by_page": gadgets_by_page,
        "life_style": life_style,
        "travels": travels,
    }

    return render(request, 'index.html', context)

def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, "Izoh muvaffaqiyatli yuborildi.")
        else:
            messages.error(request, "Ma'lumotlar noto‘g‘ri.")
    else:
        form = CommentForm()

    related_blogs = Blog.objects.filter(category=blog.category).exclude(id=blog.id)[:3]

    context = {
        'blog': blog,
        'form': form,
        'related_blogs': related_blogs,
    }

    return render(request, 'blog_single.html', context)

def blog_single(request, id):
    blog_id = get_object_or_404(Blog, id=id)
    cwg_today = Blog.objects.order_by('-id')[:3]
    author = Blog.objects.order_by('-id')[:1]

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog_id
            comment.save()
        else:
            messages.error(request, "Ma'lumotlar noto‘g‘ri.")
    else:
        form = CommentForm()

    related_blogs = Blog.objects.filter(category=blog_id.category).exclude(id=blog_id.id)[:3]

    context = {
        "cwg_today": cwg_today,
        "blog_id": blog_id,
        "author": author,
        "related_blogs": related_blogs,
        "form": form,
    }

    return render(request, 'blog_single.html', context)

def sport(request):
    return render(request, 'sport.html')

def author(request):
    return render(request, 'author.html')

def page_404(request):
    return render(request, '404.html')

def sport_life_sytle(request):
    return render(request, 'life_style.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def gallery(request):
    return render(request, 'gallery.html')

def gallery_single(request):
    return render(request, 'gallery_single.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def technology(request):
    return render(request, 'technology.html')
