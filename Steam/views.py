from django.shortcuts import render
from django.views import generic
from .models import Game

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Steam/index.html'
    context_object_name = 'latest_games_list'

    def get_queryset(self):
        return Game.objects.all().order_by('-discount_price')