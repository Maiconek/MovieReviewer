from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(response):
    return render(response, "home.html", {})

def test(response):
    return render(response, "tagformtest.html", {})

def moviesList(request):
    movie = Movie.objects.all()
    content = {"movies": Movie.objects.all()}
    return render(request, "moviesList.html", content)

def singleMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'single-movie.html', {'movie': movie}) 


def createMovie(request):
    form = MovieForm()

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Movie object was successfully created")
            return redirect('movieList')
    context = {'form': form}
    return render(request, "moviesForm.html", context)

def updateMovie(request, pk):
    movie = Movie.objects.get(id=pk) 
    form = MovieForm(instance=movie)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            print("Movie object was successfully updated")
            return redirect('movieList')
    context = {'form': form}
    return render(request, "moviesForm.html", context)

def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk) 
    movie.delete()
    return redirect('movieList')

def directorsList(request):
    director = Director.objects.all()
    content = {"directors": Director.objects.all()}
    return render(request, "directorsList.html", content)

def createDirector(request):
    form = DirectorForm()

    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Director object was successfully created")
            return redirect('directors')
    context = {'form': form}
    return render(request, "directorsForm.html", context)

def updateDirector(request, pk):
    director = Director.objects.get(id=pk)
    form = DirectorForm(instance=director)

    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES, instance=director)
        if form.is_valid():
            form.save()
            print("Director object was successfully updated")
            return redirect('directors')
    context = {'form': form}
    return render(request, "directorsForm.html", context)



def deleteDirector(request, pk):
    director = Director.objects.get(id=pk)
    director.delete()
    return redirect('directors')


def publishersList(request):
    publisher = Publisher.objects.all()
    content = {"publishers": Publisher.objects.all()}
    return render(request, "publisherList.html", content)

def createPublisher(request):
    form = PublisherForm()

    if request.method == "POST":
        form = PublisherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    
    context = {'form' : form}
    return render(request, "publishersForm.html", context)

def updatePublisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    form = PublisherForm(instance=publisher)

    if request.method == "POST":
        form = PublisherForm(request.POST, request.FILES, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    
    context = {'form' : form}
    return render(request, "publishersForm.html", context)

def deletePublisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    publisher.delete()
    return redirect('publishers')

def tagsList(request):
    tags = Tag.objects.all()
    context = {'tags' : tags}
    return render(request, "tagsList.html", context)


def createTag(request):
    form = TagForm()

    if request.method == "POST":
        form = TagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tags')
    context = {'form' : form}
    return render(request, "tagsForm.html", context)

def updateTag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)

    if request.method == "POST":
        form = TagForm(request.POST, request.FILES, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tags')
    context = {'form' : form}
    return render(request, "tagsForm.html", context)

def deleteTag(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect('tags')

def actorsList(request):
    actors = Actor.objects.all()
    context = {'actors' : actors}
    return render(request, "actorsList.html", context)

def singleActor(request, pk):
    actor = Actor.objects.get(id=pk)
    context = {'actor': actor}
    return render(request, "single-actor.html", context)

def createActor(request):
    form = ActorForm()

    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('actors')
    context = {'form' : form}
    return render(request, "actorsForm.html", context)

def updateActor(request, pk):
    actor = Actor.objects.get(id=pk)
    form = ActorForm(instance=actor)

    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actors')
    context = {'form' : form}
    return render(request, "actorsForm.html", context)

def deleteActor(request, pk):
    actor = Actor.objects.get(id=pk)
    actor.delete()
    return redirect('actors')

def addressList(request):
    address = Address.objects.all()
    context = {'address': address}
    return render(request, "addressList.html", context)

def createAddress(request):
    form = AddressForm()

    if request.method == "POST":
        form = AddressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('address')
    context = {'form' : form}
    return render(request, "addressForm.html", context)

def updateAddress(request, pk):
    address = Address.objects.get(id=pk)
    form = AddressForm(instance=address)

    if request.method == "POST":
        form = AddressForm(request.POST, request.FILES, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address')
    context = {'form' : form}
    return render(request, "addressForm.html", context)

def deleteAddress(request, pk):
    address = Address.objects.get(id=pk)
    address.delete()
    return redirect('address')

def movieTagList(request):
    movieTag = MovieTag.objects.all()
    context = {'movieTag': movieTag}
    return render(request, "movieTagList.html", context)

def createMovieTag(request):
    form = MovieTagForm()

    if request.method == "POST":
        form = MovieTagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movieTags')
    context = {'form' : form}
    return render(request, "movieTagForm.html", context)

def updateMovieTag(request, pk):
    movieTag = MovieTag.objects.get(id=pk)
    form = MovieTagForm(instance=movieTag)

    if request.method == "POST":
        form = MovieTagForm(request.POST, request.FILES, instance=movieTag)
        if form.is_valid():
            form.save()
            return redirect('movieTags')
    context = {'form' : form}
    return render(request, "movieTagForm.html", context)

def deleteMovieTag(request, pk):
    movieTag = MovieTag.objects.get(id=pk)
    movieTag.delete()
    return redirect('movieTags')

def countriesList(request):
    countries = Country.objects.all()
    context = {'countries' : countries}
    return render(request, "countriesList.html", context)

def createCountry(request):
    form = CountryForm()

    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('countries')
    context = {'form' : form}
    return render(request, "countryForm.html", context)

def updateCountry(request, pk):
    country = Country.objects.get(id=pk)
    form = CountryForm(instance=country)

    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect('countries')
    context = {'form' : form}
    return render(request, "countryForm.html", context)

def deleteCountry(request, pk):
    country = Country.objects.get(id=pk)
    country.delete()
    return redirect('countries')
