from django import forms

from Fog.models import Game, Developer, Publisher, Genre

class GameForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())
    developers = forms.ModelChoiceField(queryset=Developer.objects.all())
    publishers = forms.ModelChoiceField(queryset=Publisher.objects.all())

    class Meta:
        model = Game
        fields = ['title', 'release_date', 'price', 'description', 'image', 'genres', 'developers', 'publishers']