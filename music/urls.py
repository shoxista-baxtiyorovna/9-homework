from django.urls import path
from . import views


app_name = 'music'

urlpatterns = [
    path('list/', views.music_list, name='music_list'),
    path('create/', views.music_create, name='music_create'),
    path('detail/<int:music_id>/', views.music_detail, name='music_detail'),
    path('delete/<int:music_id>/', views.music_delete, name='music_delete'),
    path('update/<int:music_id>/', views.music_update, name='music_update'),
]