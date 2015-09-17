from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Applications, Urls

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
               'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class UrlInline(admin.TabularInline):
    model=Urls
    extra=5

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['application_name','agency']
    inlines = [UrlInline]
    list_filter = ['agency']
    search_fields = ['application_name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Applications,ApplicationAdmin)
admin.site.register(Urls)



