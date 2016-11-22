from django.contrib.auth.models import Permission
from django.db import models
from django.core.urlresolvers import reverse,reverse_lazy


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
	    return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
         return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
