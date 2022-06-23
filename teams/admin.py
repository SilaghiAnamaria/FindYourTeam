

from django.contrib import admin

from teams import models
from teams.models import Event, Player, Location, Sport

admin.site.register(Event)
admin.site.register(Player)
admin.site.register(Location)
admin.site.register(Sport)


