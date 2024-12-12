from django.urls import path
from . import views


app_name = 'sports'

urlpatterns = [
    path('list/', views.sport_list, name='sport_list'),
    path('create/', views.sport_create, name='sport_create'),
    path('detail/<int:sport_id>/', views.sport_detail, name='sport_detail'),
    path('delete/<int:sport_id>/', views.sport_delete, name='sport_delete'),
    path('update/<int:sport_id>/', views.sport_update, name='sport_update'),
]