from django.conf.urls import url
from . import views

<< << << < HEAD
app_name = 'music'
== == == =

>> >> >> > origin / master
urlpatterns = [
    # music/
    url(r'^$', views.index, name='index'),

    #music/id/
    url(r'^(?P<album_id>[0-9])+$',views.Details, name="Details"),
              << << << < HEAD

    # music/id/favourite
    url(r'^(?P<album_id>[0-9])+/favourite/$', views.favourite, name="favourite"),
== == == =
>> >> >> > origin / master
]

