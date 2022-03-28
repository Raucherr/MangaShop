from django.shortcuts import render

from main.models import Genre, Manga


def index(request):
    genres = Genre.objects.all()
    return render(request, 'main/index.html', {'genres': genres})


def manga_list(request, slug):
    books = Manga.objects.filter(genre__slug=slug)
    return render(request, 'main/book_list.html',
                                {'books': books})

