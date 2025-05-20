from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<str:day>/', views.day_view, name='day_view'),
]