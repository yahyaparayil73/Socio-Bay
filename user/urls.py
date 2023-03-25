from django.urls import path
from .import views 
app_name='user'
urlpatterns = [

    path ('home',views.user_home,name='user_home'),
    path ('user_complaints',views.user_complaints,name='user_complaints'),
    path ('login',views.user_login,name='user_login'),
    path ('signup',views.user_signup,name='user_signup'),
    path ('user_statistics',views.user_statistics,name='user_statistics'),
    path ('user_profile',views.user_profile,name='user_profile'),
    path ('test',views.test,name='test'),
    path ('user_change_password',views.user_change_password,name='user_change_password'),
    path ('chat', views.chat, name="chat"),
    path ('chat_history', views.chat_history, name="chat_history"),
    path ('user_requests', views.user_requests, name="user_requests"),
    path ('add_friend', views.add_friend, name="add_friend"),
    path ('user_logout', views.user_logout, name="user_logout"),
    path('user_email_exist', views.user_email_exist, name='user_email_exist'),





]