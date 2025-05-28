from django.urls import path
from .views import home, page_404, author, sport, sport_life_sytle, technology,login, register, blog_details, blog_single, gallery, gallery_single, contact, blog
   
    


urlpatterns = [
    path("", home, name="home"),
    path("404/", page_404, name="404"),
    path("author/", author, name="author"),
    path("sport/", sport, name="sport"),
    path("life_style/", sport_life_sytle, name="life_style"),
    path("technology/", technology, name="technology"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("gallery/", gallery, name="gallery"),
    path("gallery_single/", gallery_single, name="gallery_single"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
    path("blog/<int:id>/", blog_details, name="blog_details"),
    path("blog_single/<int:id>/", blog_single, name="blog_single"),
]
