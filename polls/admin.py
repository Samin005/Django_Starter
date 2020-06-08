from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    # list_display = ('question_text', 'pub_date')
    list_display = list(Question().__dict__.keys())[1:]


class ChoiceAdmin(admin.ModelAdmin):
    # list_display = ('question', 'choice_text', 'votes')
    list_display = list(Choice().__dict__.keys())[1:]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
