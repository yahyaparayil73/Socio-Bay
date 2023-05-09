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
    path ('user_requests', views.user_requests, name="user_requests"),
    path ('add_friend', views.add_friend, name="add_friend"),
    path ('user_logout', views.user_logout, name="user_logout"),
    path('user_email_exist', views.user_email_exist, name='user_email_exist'),
    path('profile', views.profile, name='profile'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('search_results/',views.search_results, name='search_results'),
    path('terms_of_use',views.terms_of_use, name='terms_of_use'),
    path('privacy_policy',views.privacy_policy, name='privacy_policy'),
    path('search_users/', views.search_users, name='search_users'),
    path('show_profile/user=<str:username>', views.show_profile, name='show_profile'),
    path('send-friend-request/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/', views.accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/', views.decline_friend_request, name='decline_friend_request'),
    path ('chat_history/<int:chat_id/', views.chat_history, name="chat_history"),
    path('send_message/', views.send_message, name='send_message'),

    
    
]