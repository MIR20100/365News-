from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .managers import CategoryManager 




class Category(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=200)

    
    objects = models.Manager()  
    custom = CategoryManager()

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            counter = 1
            original_slug = self.slug
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=200)  

    def __str__(self):
        return self.name

class Blog(models.Model):
    class StatusEnum(models.TextChoices):
        PUBLISHED = 'published'
        DRAFT = 'draft'

    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='Blog_images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  
    status = models.CharField(max_length=200, choices=StatusEnum.choices, default=StatusEnum.PUBLISHED)
    
    like = models.ManyToManyField(User, related_name="likes", blank=True)  
    seen = models.ManyToManyField(User, related_name="seens", blank=True)  
    hash_tag = models.ManyToManyField(Tags)
    datetime = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)  
    time = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.blog} {self.text}"
