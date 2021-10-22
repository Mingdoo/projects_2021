from .forms import MovieForm
from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie

# index
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

# create
def form(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/form.html', context)

# detail
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie':movie
    }
    return render(request, 'movies/detail.html', context)

# update
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    context = {
        'form':form,
    }
    return render(request, 'movies/form.html', context)

# delete
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
    return redirect('movies:index')