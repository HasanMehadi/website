from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song
from django.template import loader


# Create your views here.

def index(request):

   all_albums= Album.objects.all()
   context = {'all_albums':all_albums}
   return render(request, 'music/index.html', context)


def Details(request, album_id):
    album = Album.objects.get(pk=album_id)
    context ={'album':album}
    return render(request, 'music/detail.html', context)
