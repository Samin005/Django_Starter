from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_display = list(Question().__dict__.keys())[1:]
    inlines = [ChoiceInline]
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    # list_display = ('question', 'choice_text', 'votes')
    list_display = list(Choice().__dict__.keys())[1:]
    autocomplete_fields = ['question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
