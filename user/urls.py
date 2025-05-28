from django.urls import path
from .views import home, page_404, blog_single, sport, sport_life_sytle, technology_view, login_view, register_view, gallery, gallery_single, blog, index, contact


urlpatterns = [
    path("",home, name="home"),
    path("404/",page_404, name="404"),
    path("blog_single/",blog_single, name="blog_single"),
    path("sport/",sport, name="sport"),
    path("life_style/",sport_life_sytle, name="life_style"),
    path("technology/",technology_view, name="technology"),
    path("login/",login_view, name="login"),
    path("register/",register_view, name="register"),
    path("gallery/",gallery, name="gallery"),
    path("gallery_single/",gallery_single, name="gallery_single"),
    path("contact/",contact, name="contact"),
    path("blog/",blog, name="blog"),
    path("index/",index, name="index"),
]
