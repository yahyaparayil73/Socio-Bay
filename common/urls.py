from django.urls import path
from .import views 
app_name='common'

urlpatterns = [
    path ('common_home',views.common_home,name='common_home'),
    

]