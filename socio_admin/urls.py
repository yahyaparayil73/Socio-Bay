from django.urls import path
from .import views 
app_name='socio_admin'

urlpatterns = [
    path ('admin_home',views.admin_home,name='admin_home'),
    path ('admin_login',views.admin_login,name='admin_login'),



]