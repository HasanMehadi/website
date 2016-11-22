"""
from django.shortcuts import render, get_object_or_404
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
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST["song"])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album}, {'error_message': 'Please,Select a Valid Song'})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

"""

from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    # context_object_name = 'object_list'
    template_name = 'music/index.html'

    def get_queryset(self):
       return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_favorite']