"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from to_do import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('to_do.urls')),
    # path('new/', views.new_task),
    # path('filtered_data/', views.filtered_data)
    # path('films/', views.film_1),
    # path('films/', views.help_film),
    # path('help_film', views.help_film)
]
