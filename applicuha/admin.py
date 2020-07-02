from django.contrib import admin

# Register your models here.
from applicuha.models import Hall, MovieInfo, Seance, Ticket

admin.site.register(Hall)
admin.site.register(MovieInfo)
admin.site.register(Seance)
admin.site.register(Ticket)
