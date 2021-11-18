from django.urls import path
from project_1 import views


urlpatterns = [
    path('del', views.film_delete),
    path('', views.home),

]