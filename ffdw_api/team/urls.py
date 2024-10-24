from django.urls import include, path
from rest_framework import routers

from team import views

router.register(r'teams', views.TeamViewSet)