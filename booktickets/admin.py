from django.contrib import admin
from booktickets.models import Movie,Theatre,City,C_city,Show
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Theatre)
admin.site.register(C_city)
admin.site.register(City)