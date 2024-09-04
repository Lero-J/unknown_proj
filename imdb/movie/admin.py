from django.contrib import admin

from movie.models import Movie, Category, Actor

# Register your models here.
admin.site.register([Movie, Category, Actor])