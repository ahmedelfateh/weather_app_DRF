from django.contrib import admin
from .models import City

# Register your models here.


class CityAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)
