from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home' ),
    path('about/',views.about,name='about' ),
    path('solutions/',views.solutions,name='solutions' ),
    path('contact/',views.contact,name='contact' ),
    path('news/',views.news,name='news' ),
]
