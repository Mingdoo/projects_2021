from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET','POST'])
def actor_list_or_create(request):
    def actor_list():
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)

    def create_actor():
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'GET':
        return actor_list()
    elif request.method == 'POST':
        return create_actor()
    
@api_view(['GET', 'PUT', 'DELETE'])
def actor_detail_or_update_or_delete(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)

    def actor_detail():
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def update_actor():
        serializer = ActorSerializer(instance=actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete_actor():
        data = {
            'delete': f'데이터 {actor_pk}번이 삭제되었습니다.',
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return actor_detail()
    elif request.method == 'PUT':
        return update_actor()
    elif request.method == 'DELETE':
        return delete_actor()

@api_view(['GET','POST'])
def movie_list_or_create(request):
    def movie_list():
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    def create_movie():
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'GET':
        return movie_list()
    elif request.method == 'POST':
        return create_movie()

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def movie_detail():
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def update_movie():
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_movie():
        movie.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return movie_detail()
    elif request.method == 'PUT':
        return update_movie()
    elif request.method == 'DELETE':
        return delete_movie()

@api_view(['GET','POST'])
def review_list_or_create(request, movie_pk):
    def review_list():
        reviews = Review.objects\
            .prefetch_related('movie')\
            .filter(movie_id=movie_pk)

        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    def create_review():
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    
    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update_review():
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_review():
        review.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()