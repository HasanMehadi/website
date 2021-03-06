from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Registration
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #music/id/
    url(r'^(?P<pk>[0-9])+$', views.DetailView.as_view(), name="detail"),

    #Add New Album To the Database
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='add_album'),


    # music/id/favourite
    #url(r'^(?P<album_id>[0-9])+/favourite/$', views.favourite, name="favourite"),

    # Update Album using primary key
    url(r'^album/(?P<pk>[0-9])+/$', views.AlbumUpdate.as_view(), name='update_album'),

    # Delete Album using primary key and redirect to home page
    url(r'^album/(?P<pk>[0-9])+/delete/$', views.AlbumDelete.as_view(), name='delete_album')
]

