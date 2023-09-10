from django.contrib import admin
from .models import Car
# Register your models here.


class CarAdmin(admin.ModelAdmin):

    list_display= ('car_title','model', 'miles', 'year','is_featured')
    search_fields= ('car_title','model', 'miles', 'year',)
    list_filter=('car_title',)
    list_editable=('is_featured',)
    

admin.site.register(Car,CarAdmin)
