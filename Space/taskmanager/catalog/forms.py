from django import forms
from .models import Satellite, Planet, Galaxy


class SatelliteForm(forms.ModelForm):
    class Meta:
        model = Satellite
        fields = ['name', 'age', ]


class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = ['name', 'age', 'satellite', ]


class GalaxyForm(forms.ModelForm):
    class Meta:
        model = Galaxy
        fields = ['name', 'age', 'planet', ]