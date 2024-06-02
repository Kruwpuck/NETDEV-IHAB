# nih/custom_admin.py

from django.contrib.admin import AdminSite
from django.urls import path
from django.contrib.auth import views as auth_views
from .models import MyModel  # Ganti dengan model yang ingin Anda daftarkan

class CustomAdminSite(AdminSite):
    site_header = 'Custom Admin'
    site_title = 'Custom Admin Portal'
    index_title = 'Welcome to Custom Admin'

    def login(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['site_header'] = self.site_header
        return super().login(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('login/', auth_views.LoginView.as_view(template_name='custom_admin/login.html'))
        ]
        return custom_urls + urls

custom_admin_site = CustomAdminSite(name='custom_admin')

# Registrasi model Anda ke custom admin site
custom_admin_site.register(MyModel)
