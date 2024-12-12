from django.urls import path
from . import views


app_name = 'travels'

urlpatterns = [
    path('list/', views.travel_list, name='travel_list'),
    path('create/', views.travel_create, name='travel_create'),
    path('detail/<int:travel_id>/', views.travel_detail, name='travel_detail'),
    path('delete/<int:travel_id>/', views.travel_delete, name='travel_delete'),
    path('update/<int:travel_id>/', views.travel_update, name='travel_update'),
]