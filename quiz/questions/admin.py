from django.contrib import admin
from django import forms

from .models import TestSet, Question, Answer

admin.site.register(TestSet)


class AnswerInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        correct_answers = 0
        wrong_answers = 0

        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['correct_answer']:
                    correct_answers += 1
                else:
                    wrong_answers += 1

        if correct_answers == 0:
            raise forms.ValidationError('Должен быть хотя бы один правильный ответ')
        elif wrong_answers == 0:
            raise forms.ValidationError('Все ответы не могут быть правильными')


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = AnswerInlineFormset


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]


admin.site.register(Question, QuestionAdmin)
