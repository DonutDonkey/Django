from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .models import AdditionalInfo, Film, Rating
from .forms import FilmForm, AdditionalInfoForm, RatingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# from django.http import HttpResponse
# def text_response(request) :
#     return HttpResponse('<h1>First test</h1>')

def all_movies(request) :
    all_movies = Film.objects.all()
    test = 'Variable inside all_movies method'
    return render(request, 'films.html', {'film': all_movies, 'text': test})

@login_required
def new_movie(request) :
    if_new = True
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_info = AdditionalInfoForm(request.POST or None)

    if all( (form_film.is_valid(), form_info.is_valid()) ) :
        film = form_film.save(commit=False)
        info = form_info.save()

        film.additional_info = info
        film.save()

        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form_film, 'form_info': form_info, 'isNew': if_new})

@login_required
def edit_movie(request, id) :
    if_new = False
    movie = get_object_or_404(Film, pk=id) # no primary key in our model
    reviews = Rating.objects.filter(film=movie)
    actors = movie.actors.all() #actors is related name = 


    try :
        info = AdditionalInfo.objects.get(film = movie.id) # If no value is added in the models.py the dault will be lower casae name of the model
    except AdditionalInfo.DoesNotExist :
        info = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=movie)
    form_info = AdditionalInfoForm(request.POST or None, instance=info)
    form_rati = RatingForm(request.POST or None)

    if request.method == 'POST' :
        if 'stars' in request.POST :
            rating_to_save = form_rati.save(commit=False)
            rating_to_save.film = movie
            rating_to_save.save()
            
    if all( (form_film.is_valid(), form_info.is_valid()) ) :
        film = form_film.save(commit=False)
        extra = form_info.save()

        film.additional_info = extra
        film.save()

        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form_film, 'form_info': form_info, 'rating': form_rati, 'reviews': reviews, 'isNew': if_new})

@login_required
def delete_movie(request, id) :
    movie = get_object_or_404(Film, pk=id) # no primary key in our model
    
    if request.method == 'POST' :
        movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': movie})

from rest_framework import viewsets
from django.contrib.auth.models import User
from appImdbTutorial.serializers import FilmSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmViewSet(viewsets.ModelViewSet) :
    queryset = Film.objects.all()
    serializer_class = FilmSerializer