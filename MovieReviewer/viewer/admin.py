from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Director)
admin.site.register(Publisher)
admin.site.register(Movie)
admin.site.register(Tag)
admin.site.register(Actor)
admin.site.register(MovieTag)
admin.site.register(Address)
admin.site.register(Country)




