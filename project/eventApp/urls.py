from django.urls import path,include
from . import views

app_name = 'eventApp'
urlpatterns = [

    path('', views.home, name='home'),
    path('addEvent/', views.addEvent, name='addEvent'),
    path('added/', views.added, name='added'),
    path('like/', views.like, name='like'),
    path('unlike/', views.unlike, name='unlike'),



]
