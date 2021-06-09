from django.contrib import admin

from .models import Question, Choice
# Register your models here.

admin.site.site_header = "Polling Admin"
admin.site.site_title = "Polling Admin Area"
admin.site.index_title = "Welcome to the Polling admin area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInLine]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
