from django.shortcuts import render
from django.db.models import Q
from movieapp.models import Movie,UserMovie
from itertools import chain

# Create your views here.

def SearchResult(request):
    user_movie = None
    movie = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        user_movie = UserMovie.objects.filter(Q(title__contains=query))
        return render(request, 'search.html', {'query': query, 'results': user_movie})


# def SearchResult(request):
#     query = request.GET.get('q')
#     if query:
#         allMovies = UserMovie.objects.filter(title_icontains=query)
#     return render(request, 'search.html', {'query': query, 'results': allMovies})
