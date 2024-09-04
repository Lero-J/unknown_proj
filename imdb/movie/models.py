from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Actor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Movie(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    director = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    image = models.ImageField(upload_to='movie_img')
    def __str__(self):
        return f'{self.name}'



