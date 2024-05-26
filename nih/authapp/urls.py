from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('password/',views.forgot_password,name='forgot_password'),
   
]
