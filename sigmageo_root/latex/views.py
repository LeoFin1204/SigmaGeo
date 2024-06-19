from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from collection.models import UserTexList
from collection.database_connection import task

def task_list(request):

  if request.method =='POST':
    if request.user.is_authenticated:
        name = request.user.username
        id = request.POST['task_request']
        try:
          utl = UserTexList.objects.get(username=name)
          if str(id) in utl.tex_list:
            utl.tex_list = utl.tex_list.replace(str(id), '')
          else:
            utl.tex_list = utl.tex_list + str(id) + ' '
          utl.save()
        except:
          new_utl = UserTexList(username = name, tex_list = str(id))
          new_utl.save()

  name = request.user.username
  try:
    utl = list(map(int, UserTexList.objects.get(username = name).tex_list.split()))
  except:
    utl = []

  context = {
    'title': 'Список задач',
    'is_admin': request.user.groups.filter(name='admin').exists(),
    'task_list': [task(id) for id in utl],
  }

  return render(request, 'pages/task_list.html', context)


def compile(request):
  
  context = {
    'title': 'Компиляция',
    'is_admin': request.user.groups.filter(name='admin').exists()
  }

  return render(request, 'pages/compile.html', context)

def p404(request, *args, **kwargs):
  return render(request, 'pages/404.html', {'title': 'Ошибка'})