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
   
   
    path('driveroffleat/',DriverOfFleatAPI.as_view(),name="listing-all-drivers-under-fleats"),
    path('driveroffleat/<str:id>/',DriverOfFleatAPI.getByID,name="listing-particular-drivers-under-fleats"),
    path('driveroffleatsetfleat/',DriverOfFleatAPI.setFleat,name="setting-up-owner"),
    path('driveroffleatsetambulance/',DriverOfFleatAPI.setAmbulance,name="setting-up-ambulance"),
    path('driveroffleatgetfleatandambulance/',DriverOfFleatAPI.AmbulanceAndFleatID,name="getting-ambulance and fleat id"),


    path('firstArrived/<str:id>/',check,name='Checking-First-Arrived'),

    # path('first/<str:id>/',UserAPI.firsAppeared,name='If-appeared-first-time'),
]
