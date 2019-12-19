from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(VegetableModel)
admin.site.register(WeatherModel)
admin.site.register(GrowModel)
admin.site.register(GardenModel)
admin.site.register(UserProfileModel)
admin.site.register(ParcelModel)