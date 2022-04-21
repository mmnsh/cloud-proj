from django.contrib import admin
from apis1.models import plane, airport, carrier, flight

class AdminMode(admin.ModelAdmin):
    list_display = ['flight_datetime', 'flight_price', 'flight_class', 'flight_source_city',
                    'flight_destination_city', 'flight_carrier', 'flight_datetime']
    search_fields = ['flight_datetime', 'flight_price']

admin.site.register(plane)
admin.site.register(airport)
admin.site.register(carrier)
admin.site.register(flight, AdminMode)