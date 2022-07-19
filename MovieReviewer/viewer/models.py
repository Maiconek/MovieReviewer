from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born = models.DateField()
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey('Address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL, blank=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField()
    rating = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

    countries = models.ManyToManyField('Country', blank=True)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class MovieTag(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie) + ", tags: " + str(self.tag)

class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born = models.DateField()
    nationality = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Address(models.Model):
    number = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.apartment_number is None:
            if self.state is None:
                return str(self.number) + " " + str(self.street) + ", "+ str(self.city) + " " + str(self.zip_code) + ", " + str(self.country)
            else:
                return str(self.number) + " " + str(self.street) + ", "+ str(self.city) + ", " + str(self.state) + " " + str(self.zip_code) + ", " + str(self.country)
        else:
            return str(self.number) + " " + str(self.street) + " " + str(self.apartment_number) + ", " + str(self.city) 
            + ", " + str(self.state) + " " + str(self.zip_code) + ", " + str(self.country)
