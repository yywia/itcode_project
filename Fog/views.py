from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from rest_framework import viewsets


from Fog.forms import GameForm
from Fog.models import Game, Publisher, Developer, Genre, Statistics
from Fog import filters, serializers

# Create your views here.
class PublisherAPI(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = serializers.Publisher

class GameAPI(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = serializers.Game

class DeveloperAPI(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = serializers.Developer

class GenreAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.Genre

class StatisticsAPI(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = serializers.Statistics

class GamesList(FilterView):
    template_name = 'Fog/games_list.html'
    model = Game
    context_object_name = 'games'
    filterset_class = filters.Game


class GamesDetail(DetailView):
    template_name = 'Fog/game_detail.html'
    model = Game
    context_object_name = 'game'

class GamesUpdate(UpdateView):
    template_name = 'Fog/game_update.html'
    model = Game
    form_class = GameForm

    def get_success_url(self):
        return reverse_lazy('game_detail', kwargs={'pk': self.object.pk})

class GamesDelete(DeleteView):
    template_name = 'Fog/game_delete.html'
    model = Game
    success_url = reverse_lazy('games_list')

class GamesCreate(CreateView):
    template_name = 'Fog/game_create.html'
    model = Game
    fields = ['title', 'release_date', 'price', 'description', 'image']
    success_url = reverse_lazy('games_list')

def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('games_list')
    else:
        form = GameForm()
    return render(request, 'Fog/game_create.html', {'form': form})