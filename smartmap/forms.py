from django.forms import ModelForm

from smartmap.models import Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
