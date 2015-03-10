from django.contrib import admin
from .models import (Link)

class LinkAdmin(admin.ModelAdmin):

    list_display = ['url_original' ,'url_generated']
    search_fields = ['url_original', 'url_generated']
    prepopulated_fields = {'url_generated': ('url_original',)}

admin.site.register(Link, LinkAdmin)