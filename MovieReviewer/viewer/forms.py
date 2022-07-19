from django import forms
from django.forms import ModelForm, Select
from .models import *
from MovieReviewer import settings

class MovieForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=False)
    class Meta:
        model = Movie
        fields = ['title', 'director', 'publisher', 'description', 'year', 'rating', 'countries']
        
    
class DirectorForm(ModelForm):
    born = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y", 
    attrs={'placeholder': 'Enter a date in day/month/year format'}),
    input_formats=('%d/%m/%Y', ))

    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'born', 'nationality']

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class ActorForm(ModelForm):
    born = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y", 
    attrs={'placeholder': 'Enter a date in day/month/year format'}),
    input_formats=('%d/%m/%Y', ))
    
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'born', 'nationality', 'movies']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['number', 'street', 'apartment_number', 'city', 'state', 'zip_code', 'city', 'country']

class MovieTagForm(ModelForm):
    class Meta: 
        model = MovieTag
        fields = ['movie', 'tag']

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name']
