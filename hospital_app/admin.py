from django.contrib import admin
from .models import Doctor,DoctorCategory,Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(DoctorCategory)
admin.site.register(Appointment)