from django.core import serializers
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe
from .models import Genre, Movie
from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    paginator = Paginator(movies, 10)
    page = request.GET.get('page')
    pagination_obj = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        context = {
            'movies': pagination_obj
        }
        data = serializers.serialize('json', pagination_obj)
        return HttpResponse(data, content_type='application/json')
    else:
        context = {
            'movies': pagination_obj,
        }
        return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def recommended(request):
    movies = get_list_or_404(Movie)
    movies1 = Movie.objects.all()[:25]
    movies2 = Movie.objects.all()[25:50]
    movies3 = Movie.objects.all()[50:75]
    movies4 = Movie.objects.all()[75:]
    
    #algorithm
    if request.method == 'GET':
        context = {
            'movies1' : movies1,
            'movies2' : movies2,
            'movies3' : movies3,
            'movies4' : movies4,
        }
        return render(request, 'movies/recommended.html', context)
    elif request.method == 'POST':
        selected = []
        for value in request.POST:
            if value.startswith('movie'):
                selected.append(request.POST[value])
        
        selected_genres = set()
        for pk in selected:
            genres = Genre.objects.filter(movie__id=int(pk))
            for genre in genres:
                selected_genres.add(genre.id)

        recommended_movies = Movie.objects.filter(genres__in = selected_genres).order_by('-vote_average').distinct()[:10]
        context = {
            'movies': recommended_movies,
        }
        return render(request, 'movies/recommended.html', context)
    