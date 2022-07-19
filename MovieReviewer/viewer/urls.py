from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('movies', views.moviesList, name='movieList'),
    path('single-movie/<str:pk>/', views.singleMovie, name='single-movie'),
    path('create-movie', views.createMovie, name='create'),
    path('update-movie/<str:pk>/', views.updateMovie, name='update'),
    path('delete-movie/<str:pk>/', views.deleteMovie, name='delete'),
    path('directors', views.directorsList, name='directors'),
    path('create-director', views.createDirector, name='create-director'),
    path('update-director/<str:pk>/', views.updateDirector, name='update-director'),
    path('delete-director/<str:pk>/', views.deleteDirector, name='delete-director'),
    path('publishers', views.publishersList, name='publishers'),
    path('create-publisher', views.createPublisher, name='create-publisher'),
    path('update-publisher/<str:pk>/', views.updatePublisher, name='update-publisher'),
    path('delete-publisher/<str:pk>/', views.deletePublisher, name='delete-publisher'),
    path('tags', views.tagsList, name='tags'),
    path('create-tag', views.createTag, name='create-tag'),
    path('update-tag/<str:pk>/', views.updateTag, name='update-tag'),
    path('delete-tag/<str:pk>/', views.deleteTag, name='delete-tag'),
    path('actors', views.actorsList, name='actors'),
    path('single-actor/<str:pk>/', views.singleActor, name='single-actor'),
    path('create-actor', views.createActor, name='create-actor'),    
    path('update-actor/<str:pk>/', views.updateActor, name='update-actor'),
    path('delete-actor/<str:pk>/', views.deleteActor, name='delete-actor'),
    path('addressList', views.addressList, name='address'),
    path('create-address', views.createAddress, name='create-address'),
    path('update-address/<str:pk>/', views.updateAddress, name='update-address'),
    path('delete-address/<str:pk>/', views.deleteAddress, name='delete-address'),
    path('movieTags', views.movieTagList, name='movieTags'),
    path('create-movieTag', views.createMovieTag, name='create-movieTag'),
    path('update-movieTag/<str:pk>/', views.updateMovieTag, name='update-movieTag'),
    path('delete-movieTag/<str:pk>/', views.deleteMovieTag, name='delete-movieTag'),
    path('countries', views.countriesList, name='countries'),
    path('create-country', views.createCountry, name='create-country'),
    path('update-country/<str:pk>/', views.updateCountry, name='update-country'),
    path('delete-country/<str:pk>/', views.deleteCountry, name='delete-country'),
    path('test', views.test, name='test')
]