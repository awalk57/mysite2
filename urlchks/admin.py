from django.contrib import admin

from .models import Applications, Urls
# Register your models here.
class UrlInline(admin.TabularInline):
    model=Urls
    extra=5

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['application_name','agency']
    inlines = [UrlInline]
    list_filter = ['agency']
    search_fields = ['application_name']

admin.site.register(Applications,ApplicationAdmin)
admin.site.register(Urls)
