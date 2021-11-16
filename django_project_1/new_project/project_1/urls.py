from django.urls import path
from project_1 import views


urlpatterns = [
    path('', views.home)
]