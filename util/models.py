from django.db import models

class Subscribe(models.Model):
    email = models.EmailField()

class Partners(models.Model):
    logo = models.ImageField(upload_to='partners/')

class Contact(models.Model):
    instagram = models.URLField()
    telegram = models.URLField()  # <-- tuzatildi
    youtube = models.URLField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)  # <-- max_length qo‘shildi

class ContactUs(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()  # <-- tuzatildi
