from django.contrib import admin
from .models import Drone,DroneCategory,Competition,Pilot
# Register your models here.
admin.site.register(Drone)
admin.site.register(DroneCategory)
admin.site.register(Pilot)
admin.site.register(Competition)
