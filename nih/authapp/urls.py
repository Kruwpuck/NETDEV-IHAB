from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('choose_seat/<int:movie_id>/', views.choose_seat, name='choose_seat'),
]
