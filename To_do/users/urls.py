from django.urls import path
from users import views

urlpatterns = [
    path('create-user/', views.create_user, name='create'),
    path('profile_view/', views.profile_view, name='view-profile'),
    path('user_login/', views.user_login, name='user-login'),
]
