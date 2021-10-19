from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Page

class PageAdmin(VersionAdmin):
    search_fields = ['name']
    list_display = ('name','description')
admin.site.register(Page, PageAdmin)
