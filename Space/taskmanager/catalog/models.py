from django.db import models
import uuid  # Required for unique book instances
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.

class Satellite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular satellite")
    name = models.CharField(max_length=200, help_text="Enter the name of the satellite")
    age = models.CharField(max_length=200, help_text="Enter the age of the satellite")

    def __str__(self):
        return '%s, %s' % (self.name, self.age)

    def get_absolute_url(self):
        return reverse('Satellite-items', args=[str(self.id)])


class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular planet")
    name = models.CharField(max_length=200, help_text="Enter the name of the planet")
    age = models.CharField(max_length=200, help_text="Enter the age of the planet")
    satellite = models.ForeignKey('Satellite', on_delete=models.SET_NULL, null=True, help_text="Enter the id of the satellite")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s (%s)' % (self.name, self.satellite.name)

    def get_absolute_url(self):
        return reverse('Planet-items', args=[str(self.id)])


class Galaxy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular car")
    name = models.CharField(max_length=200, help_text="Enter the name of the car")
    age = models.CharField(max_length=200, help_text="Enter the brand of the car")
    planet = models.ForeignKey('Planet', on_delete=models.SET_NULL, null=True, help_text="Enter the id of the planet")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return '%s (%s)' % (self.name, self.planet.name)