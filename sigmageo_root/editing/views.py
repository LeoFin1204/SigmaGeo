from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import TaskEditor
from collection.database_connection import task
from collection.models import Problem

def add_task(request):
  
  if request.method == 'POST':
    new_task = Problem(num = request.POST['num'],
                       grade = request.POST['grade'],
                       text = request.POST['text'],
                       solution = request.POST['solution'],
                       themes = request.POST['themes'],
                       source = request.POST['source'],
                       year = request.POST['year'],
                       stage = request.POST['stage'],
                       author = request.POST['author'],
                       dif = int(request.POST['dif']))
    new_task.save()

  context = {
    'title': 'Новая задача',
    'is_admin': request.user.groups.filter(name='admin').exists(),
  }

  return render(request, 'pages/add_task.html', context)

def redact_task(request):

  id = request.GET['id']

  if request.method == 'POST':
    problem = Problem.objects.get(id = id)
    problem.num = request.POST['num']
    problem.grade = request.POST['grade']
    problem.text = request.POST['text']
    problem.solution = request.POST['solution']
    problem.themes = request.POST['themes']
    problem.source = request.POST['source']
    problem.year = request.POST['year']
    problem.stage = request.POST['stage']
    problem.author = request.POST['author']
    problem.dif = int(request.POST['dif'])
    problem.save(update_fields=['num', 'grade', 'text', 'solution', 'themes', 'source', 'year', 'stage', 'author', 'dif'])
    
    return HttpResponseRedirect(f'/sigma_geo/problem?id={id}')

  context = {
    'title': 'Редактирование',
    'is_admin': request.user.groups.filter(name='admin').exists(),
    'task': task(id),
  }

  return render(request, 'pages/redact_task.html', context)

def add_section(request):

  context = {
    'title': 'Новый раздел',
    'is_admin': request.user.groups.filter(name='admin').exists()
  }

  return render(request, 'pages/add_section.html', context)

def redact_section(request):

  context = {
    'title': 'Редактирование',
    'is_admin': request.user.groups.filter(name='admin').exists()
  }

  return render(request, 'pages/redact_section.html', context)

def p404(request, *args, **kwargs):
  return render(request, 'pages/404.html', {'title': 'Ошибка'})