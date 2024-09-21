# my_app/urls.py
from django.urls import path
from . import views
from django.contrib import admin  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('create/', views.createpage, name='create'),
    path('profile/',views.profilepage,name='profile'),
    path('',views.homepage,name='home'),
    path('logout/',views.logoutprofile,name='logout'),
    path('update/',views.updatepage,name='update'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  