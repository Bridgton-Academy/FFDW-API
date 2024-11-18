from django.urls import path
from . import views

urlpatterns = [
    path('gameTeamRound/', views.gameTeamRound, name='gameTeamRound'),
]