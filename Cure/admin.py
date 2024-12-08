from django.contrib import admin
from .models import Contact
from .models import InternshipApplication
from django.contrib import admin
from .models import Appointment
# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'preferred_date', 'preferred_time', 'created_at')
    search_fields = ('full_name', 'department', 'contact_number', 'email')
    list_filter = ('department', 'preferred_date')




@admin.register(InternshipApplication)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'start_date', 'areas_of_interest')
    search_fields = ('name', 'email')
    list_filter = ('areas_of_interest',)
    ordering = ('-start_date',)



admin.site.register(Contact)
