from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = [
            'city',
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
        }

    # def clean_city(self):
    #     city = self.cleaned_data.get('city', False)
    #     if not self.instance.city == city:
    #         # validate image
    #     return None
