<< << << < HEAD
from django.shortcuts import render, get_object_or_404
== == == =
from django.shortcuts import render
>> >> >> > origin / master
from django.http import HttpResponse
from .models import Album, Song
from django.template import loader


# Create your views here.

def index(request):

   all_albums= Album.objects.all()
   context = {'all_albums':all_albums}
   return render(request, 'music/index.html', context)


def Details(request, album_id):

    << << << < HEAD
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

== == == =
album = Album.objects.get(pk=album_id)
context = {'album': album}
return render(request, 'music/detail.html', context)
>> >> >> > origin / master
