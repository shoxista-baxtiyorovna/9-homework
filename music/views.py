from django.shortcuts import render, redirect, get_object_or_404
from .models import Music


def home(request):
    return render(request, 'index.html')

def music_list(request):
    tracks = Music.objects.all()
    ctx = {'tracks': tracks}
    return render(request, 'music/music_list.html', ctx)


def music_create(request):
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        if album_title and artist and release_date and genre:
            Music.objects.create(
                album_title=album_title,
                artist=artist,
                release_date=release_date,
                genre=genre
            )
            return redirect('music:music_list')
    return render(request, 'music/music_form.html')


def music_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    ctx = {'music': music}
    return render(request, 'music/music_detail.html', ctx)

def music_delete(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    music.delete()
    return redirect('music:music_list')

def music_update(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        if album_title and artist and release_date and genre:
            music.album_title = album_title
            music.artist = artist
            music.release_date = release_date
            music.genre = genre
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'music/music_form.html', ctx)
