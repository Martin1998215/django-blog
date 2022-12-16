from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.mypost, name='mypost'),
    path('contacts/', views.contact, name='contact'),
    path('<slug:slug>/', views.main, name='main')

]

urlpatterns += staticfiles_urlpatterns()
