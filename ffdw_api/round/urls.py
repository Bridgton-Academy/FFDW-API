from django.urls import path
from . import views

urlpatterns = [
    path('round/', views.round, name='round'),
]