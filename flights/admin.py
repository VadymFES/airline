from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

class AirportAdmin(admin.ModelAdmin):
    list_display = ("code", "city")

admin.site.register(Airport, AirportAdmin)    # this will allow us to see the airports in the admin page
admin.site.register(Flight, FlightAdmin)     # this will allow us to see the flights in the admin page
admin.site.register(Passenger, PassengerAdmin)  # this will allow us to see the passengers in the admin page