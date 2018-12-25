from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Album


# Homepage


class AlbumListView(generic.ListView):
    # queryset = Album.objects.all()
    model = Album
    # template = 'music/home.html'


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/album_detail.html'


def home(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }
    return render(request, 'music/home.html', context)
    # return HttpResponse('<h1>This is Music section page</h1>')


def redirect_to_youtube(request):
    return redirect('https://www.youtube.com/')
