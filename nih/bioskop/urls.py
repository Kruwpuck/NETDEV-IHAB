from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    #path('buy-ticket/', views.movie_list, name='buy-ticket'),
    path('movies/', views.movie_list, name='movie_list'),
    path('choose-seat/<int:movie_id>/', views.choose_seat, name='choose_seat'),
    path('payment/', views.payment, name='payment'),  # Tambahkan path untuk view payment
    path('payment/success/', views.payment_success, name='payment_success'),  # Tambahkan path untuk view payment_success
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)