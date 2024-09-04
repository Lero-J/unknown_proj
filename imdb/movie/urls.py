from django.urls import path

from movie import views

urlpatterns = [
    path('', views.addMovie, name='index'),
    path('movie_info/<int:movie_id>', views.movieInfo, name='movie_info')
    # path('addMovie', views.addMovie, name='addMovie')
]


