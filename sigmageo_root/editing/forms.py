from django import forms
from collection.models import Problem

class TaskEditor(forms.ModelForm):

  class Meta:
    model = Problem
    fields = '__all__'
    widgets = {}
    labels = {
      'num' : 'Номер',
      'grade' : 'Класс',
      'text' : 'Условие',
      'solution' : 'Решение',
      'themes' : 'Темы',
      'source' : 'Источник',
      'year' : 'Год',
      'stage' : 'Этап',
      'author' : 'Автор',
      'dif' : 'Сложность',
    }