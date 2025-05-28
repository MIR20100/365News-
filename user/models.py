from django.db import models

# Create your models here.
class Author(models.Model):

    class RoleChoice(models.TextChoices):
        ADMIN = 'admin'
        WRITER = 'writer'
    image = models.ImageField(upload_to='Author/')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio =  models.TextField()
    role = models.CharField(max_length=20, choices = RoleChoice.choices,default=RoleChoice.ADMIN)