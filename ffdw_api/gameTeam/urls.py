from django.urls import path
from . import views

urlpatterns = [
    path('gameTeam/', views.gameTeam, name='gameTeam'),
]