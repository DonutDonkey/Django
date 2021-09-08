from django.forms import ModelForm
from .models import AdditionalInfo, Film

class FilmForm(ModelForm) :
    class Meta:
        model = Film
        fields = ['title', 'year', 'description', 'release', 'imdb_rating', 'poster']

class AdditionalInfoForm(ModelForm) :
    class Meta:
        model = AdditionalInfo
        fields = ['genre', 'duration_time']