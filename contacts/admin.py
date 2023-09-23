from django.contrib import admin
from .models import Contacts
# Register your models here.


class ContactsAdmin(admin.ModelAdmin):

    list_display= ('id','car_title','first_name', 'last_name', 'email','city')
    search_fields= ('car_title','city',)
    list_filter=('car_title',)
    list_per_page = 25

    



admin.site.register(Contacts,ContactsAdmin)