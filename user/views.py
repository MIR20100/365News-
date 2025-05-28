from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages

from django.contrib.auth import authenticate,login

def home(request):
    
    return render(request,'index.html')

def author(request):
    return render(request,'author.html')

def page_404(request):
    return render(request,'404.html')

def blog_single(request):
    


    return render(request,'blog_single.html')

def sport(request):
    return render(request,'sport.html')

def sport_life_sytle(request):
    return render(request,'life_style.html')

def technology_view(request):
    return render(request,'technology.html')

def gallery(request):
    return render(request,'gallery.html')

def gallery_single(request):
    return render(request,'gallery_single.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user =authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.add_message(request,messages.ERROR,"user not found")
        else:   
            messages.add_message(request,messages.ERROR,"user not found")
          
    return render(request,'login.html')



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            messages.add_message(request,level=messages.ERROR,message=form.errors)
             

    return render(request,'register.html')
