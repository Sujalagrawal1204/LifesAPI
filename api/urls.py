from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('drivers/',DriverAPI.as_view()),
    path('driver/<str:id>/',DriverAPI.getDriver,name='getting-particular'),
    
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('users/',UserAPI.as_view()),
    
    path('ambulances/',AmbulanceAPI.as_view()),
    path('ambulanceid/<str:id>/',AmbulanceAPI.ambulanceId,name='getting-by-Id'),
    
    path('fleats/',FleatAPI.as_view()),
    path('updateambulancestatus/<str:id>/',AmbulanceAPI.updateBusy,name='busy-status-update-ambulance'),
    path('updateambulancefirst/<str:id>/',AmbulanceAPI.updateFirst,name='busy-status-update-ambulance'),
    path('updatedriverstatus/<str:id>/',DriverAPI.updateBusy,name='busy-status-update-driver'),
    
    path('firstArrived/<str:id>/',check,name='Checking-First-Arrived'),

    # path('first/<str:id>/',UserAPI.firsAppeared,name='If-appeared-first-time'),
]
