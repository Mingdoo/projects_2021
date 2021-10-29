from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name',)

class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title',)

class MovieSerializer(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'id')
    actors = ActorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path', 'actors', 'reviews')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('movie_id', 'pk', 'title', 'content', 'rank')

class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class ActorSerializer(serializers.ModelSerializer):
            class Meta:
                model = Actor
                fields = ('name',)
        actors = ActorSerializer(many=True, read_only=True)
        class Meta:
            model = Movie
            fields = '__all__'
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'