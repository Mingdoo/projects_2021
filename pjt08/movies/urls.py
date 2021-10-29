from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('actors/', views.actor_list_or_create, name='actors'),
    path('actors/<int:actor_pk>/', views.actor_detail_or_update_or_delete, name='actor_detail'),
    path('movies/', views.movie_list_or_create, name='movies'),
    path('movies/<int:movie_pk>/', views.movie_detail_or_update_or_delete, name='movie_detail'),
    path('movies/<int:movie_pk>/reviews/', views.review_list_or_create, name='reviews'),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail_or_update_or_delete, name='review_detail'),
]
