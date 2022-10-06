from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movie/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movie/detail.html', context)

def create(request):
    if request.method == 'POST':
        movie = MovieForm(request.POST)
        if movie.is_valid():
            movie_detail = movie.save()
            return redirect('movie:detail', movie_detail.pk)
    else:
        movie = MovieForm()
    context = {
        'movie': movie,
    }
    return render(request, 'movie/form.html', context)

def update(request, pk):
    movie_pick = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie = MovieForm(request.POST, instance=movie_pick)
        if movie.is_valid():
            movie_detail = movie.save()
            return redirect('movie:detail', movie_detail.pk)
    else:
        movie = MovieForm(instance=movie_pick)
    context = {
        'movie': movie,
        'movie_pick': movie_pick,
    }
    return render(request, 'movie/form.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movie:index')

