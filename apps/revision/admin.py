from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Page, AutoResponse, MatchingText

class PageAdmin(VersionAdmin):
    search_fields = ['name']
    list_display = ('name','description')
admin.site.register(Page, PageAdmin)

class AutoResponseAdmin(VersionAdmin):
    search_fields = ['response']
    list_display = ('response',)
admin.site.register(AutoResponse, AutoResponseAdmin)

class MatchingTextAdmin(VersionAdmin):
    search_fields = ['title']
    list_display = ('auto_response', 'title',)
admin.site.register(MatchingText, MatchingTextAdmin)