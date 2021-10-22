from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
'''
R
index

R
detail

    D
    delete

    U
    edit : update

C
new :create

'''

def index(request):
    movies = Movie.objects.all()

    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('movies:index')

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/edit.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')

    movie = Movie(title=title, overview=overview, poster_path=poster_path)
    movie.save()

    return redirect('movies:detail', movie.pk)

def update(request, pk):
    
    movie = Movie.objects.get(pk=pk)

    movie.title = request.POST.get('title')
    movie.overview = request.POST.get('overview')
    movie.poster_path = request.POST.get('poster_path')

    movie.save()

    return redirect('movies:detail', movie.pk)

def search(request):
    search = request.GET.get('search')
    
    movies = Movie.objects.filter(title__contains=search)

    context = {
        'search' : search,
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)
    
    