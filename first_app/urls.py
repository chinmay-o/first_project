from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [

    path('access_log/', views.home, name="home"),
    path('help', views.help, name="help"),
    path('users/', views.users, name="users"),
    path('home/', views.form_name, name="forms"),
    path('user_logout/', views.user_logout, name="user_logout"),
]
