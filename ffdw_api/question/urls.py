from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.question, name='question'),
    path('question/<int:pk>/', views.individual_question, name='individual_question'),
]