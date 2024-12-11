from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
    path('update/<int:movie_id>/', views.movie_update, name='movie_update'),
]