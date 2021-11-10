from django.urls import path
from to_do import views

urlpatterns = [
    path('', views.home),
    path('present/', views.present),
    path('greeting', views.greeting),
    path('introduction', views.introduction),
    path('time',views.time),
    path('solution_task',views.solution_task),
]
