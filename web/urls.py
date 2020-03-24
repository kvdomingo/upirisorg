from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('members', views.members, name='members'),
    path('members/<str:mem_href>', views.member, name='member'),
    path('alumni', views.construction, name='alumni'),
    path('gallery', views.construction, name='gallery'),
    path('contact', views.construction, name='contact'),
]
