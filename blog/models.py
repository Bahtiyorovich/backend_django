from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
#     genre = models.ForeignKey(BookGenre, null=True, on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



