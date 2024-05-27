from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/galaxy', views.showGalaxy, name='showGalaxy'),
    path('show/planet', views.showPlanet, name='showPlanet'),
    path('show/satellite', views.showSatellite, name='showSatellite'),
    path('create/galaxy', views.createGalaxy, name='createGalaxy'),
    path('create/planet', views.createPlanet, name='createPlanet'),
    path('create/satellite', views.createSatellite, name='createSatellite'),
    path('update/galaxy', views.updateGalaxy, name='updateGalaxy'),
    path('update/planet', views.updatePlanet, name='updatePlanet'),
    path('update/satellite', views.updateSatellite, name='updateSatellite'),
]