from gc import get_objects
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

from .models import Satellite, Planet, Galaxy
from .forms import SatelliteForm, PlanetForm, GalaxyForm


def index(request):
    # Функция отображения для домашней страницы сайта.

    # Генерация "количеств" некоторых главных объектов
    num_satellite = Satellite.objects.all().count()
    num_planet = Planet.objects.all().count()
    num_galaxy = Galaxy.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_galaxy': num_galaxy, 'num_planet': num_planet, 'num_satellite': num_satellite},
    )


def showGalaxy(request):
    return render(
        request,
        'showGalaxy.html',
        context={'Galaxy': Galaxy.objects.all()},
    )


def showPlanet(request):
    return render(
        request,
        'showPlanet.html',
        context={'Planet': Planet.objects.all()},
    )


def showSatellite(request):
    return render(
        request,
        'showSatellite.html',
        context={'Satellite': Satellite.objects.all()},
    )


def createGalaxy(request):
    form = GalaxyForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(
        request,
        'create.html',
        context={'form': form, }
    )


def createPlanet(request):
    form = PlanetForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(
        request,
        'create.html',
        context={'form': form, }
    )


def createSatellite(request):
    form = SatelliteForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(
        request,
        'create.html',
        context={'form': form, }
    )


def updateGalaxy(request):
    Galaxyid = request.GET['id']
    instance = Galaxy.objects.get(id=Galaxyid)
    form = GalaxyForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(
        request,
        'update.html',
        context={'instance': instance, 'form': form}
    )


def updatePlanet(request):
    Planetid = request.GET['id']
    instance = Planet.objects.get(id=Planetid)
    form = PlanetForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(
        request,
        'update.html',
        context={'instance': instance, 'form': form}
    )


def updateSatellite(request):
    Satelliteid = request.GET['id']
    instance = Satellite.objects.get(id=Satelliteid)
    form = SatelliteForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(
        request,
        'update.html',
        context={'instance': instance, 'form': form}
    )