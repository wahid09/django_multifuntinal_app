from django.urls import path
from App_Login import views


app_name = 'App_Login'


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile', views.user_info_update, name='update_profile'),
    path('password/', views.pass_change, name='pass_change')
]