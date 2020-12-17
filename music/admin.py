from django.contrib import admin

# Register your models here.

# admin.site.register(Admin)
from music.models import Band, Musician

admin.site.register(Band)
admin.site.register(Musician)
