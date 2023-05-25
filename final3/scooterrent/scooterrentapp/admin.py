from django.contrib import admin
from .models import Scooter,Booking

admin.site.site_header = "unni"
admin.site.site_title = "Admin Panel"

@admin.register(Scooter)
class ScooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'kilometer_range', 'price')
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'scooter', 
                    'start_datetime', 'end_datetime')
    search_fields = ('name', 'start_datetime', 'end_datetime')
    list_filter = ('scooter',)
