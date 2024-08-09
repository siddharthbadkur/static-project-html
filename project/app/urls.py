from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('blogs/',blogs,name='blogs')
   
]