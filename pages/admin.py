from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def photo (self, object):
        return format_html('<img src="{}" width="40" style=" border-radius: 10px " />'.format(object.image.url))
    
    list_display = ('id', 'photo' , 'first_name', 'designation', 'created')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'designation','last_name', )
    list_filter = ('designation',)

admin.site.register(Team,TeamAdmin)