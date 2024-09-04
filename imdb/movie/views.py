from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from movie.forms import MovieForm
from movie.models import Movie, Category, Actor


# Create your views here.



# def index(request):
#     movies = Movie.objects.all()
#     categories = Category.objects.all()
#
#     actors = Actor.objects.all()
#     ctx = {
#         'movies':movies,
#         'categories':categories,
#         'actors': actors
#     }
#
#     return render(request, 'movie/layouts/base.html', context=ctx)


def addMovie(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()
    actors = Actor.objects.all()
    searched_movies = Movie.objects.filter(name__startswith=request.POST['search_block'])
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'movie/layouts/base.html', context={
        'form':MovieForm(),
        'movies':movies,
        'categories':categories,
        'actors': actors
    })


def movieInfo(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie_categories = movie.category.all()
    ctx = {
        'movie' : movie,
        'movie_categories' : movie_categories
    }
    return render(request,'movie/movie_info.html', context=ctx)

def searching(request):



