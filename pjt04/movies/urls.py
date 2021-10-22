from django.urls import path
from . import views

app_name = 'movies'
'''
index

detail
    delete
    edit : update

new :create

'''
urlpatterns = [
    path('', views.index, name='index'),
    
    #detail
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),

    #new
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #search
    path('search/', views.search, name='search')
]

