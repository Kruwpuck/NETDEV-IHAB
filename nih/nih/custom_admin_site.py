from django.contrib.admin import AdminSite
from .models import MyModel

class CustomAdminSite(AdminSite):
    site_header = 'Custom Admin'
    site_title = 'Custom Admin Portal'
    index_title = 'Welcome to Custom Admin'

custom_admin_site = CustomAdminSite(name='custom_admin')
