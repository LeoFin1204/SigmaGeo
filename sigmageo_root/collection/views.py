from django.http import HttpResponseRedirect
from django.shortcuts import render
from .database_connection import subsection_tasks, all_subsection, task, search_database, last_page
from .models import UserTexList
from .models import Problem, Olimp, Book, Theme

CASE = {
  'olimps': 'Олимпиады',
  'books': 'Книги и журналы',
  'themes': 'Тематические листочки',
}

def main(request):

  print(request)

  context = {
    'title': 'SigmaGeo',
    'is_admin': request.user.groups.filter(name='admin').exists(),
  }

  return render(request, 'pages/main.html', context)

def subsection(request, section):
  
  if not section in ['olimps', 'books', 'themes']:
    return render(request, 'pages/404.html', {'title' : 'Ошибка'})

  if request.method =='POST':
    id = int(request.GET['id'])
    if request.user.is_authenticated:
        name = request.user.username
        try:
          utl = UserTexList.objects.get(username=name)
          if str(id) in utl.tex_list:
            utl.tex_list = utl.tex_list.replace(str(id) + ' ', '')
          else:
            utl.tex_list += str(id) + ' '
          utl.save()
        except:
          new_utl = UserTexList(username = name, tex_list = str(id))
          new_utl.save()

  subsect = request.GET['subsection']
  try:
    page = int(request.GET['page'])
  except:
    return HttpResponseRedirect(f'?subsection={subsect}&page=1')

  l_page = last_page(subsect)

  context = {
    'title': CASE[section],
    'is_admin': request.user.groups.filter(name='admin').exists(),
    'task_list': subsection_tasks(subsect, page),
    'section': section,
    'pages': [page-1, page, page+1 if page+1 <= l_page else 0],
    'link': f'?subsection={subsect}&page=',
    'last_page': l_page,
  }

  return render(request, 'pages/subsection.html', context)

def section(request, section):

  if not section in ['olimps', 'books', 'themes']:
    return render(request, 'pages/404.html', {'title' : 'Ошибка'})

  context = {
    'title': CASE[section],
    'is_admin': request.user.groups.filter(name='admin').exists(),
    'subsection_list': all_subsection(section),
    'section': section,
  }

  return render(request, 'pages/section.html', context)


def problem(request):

  id = int(request.GET['id'])

  if request.method =='POST':
    if request.user.is_authenticated:
        name = request.user.username
        try:
          utl = UserTexList.objects.get(username=name)
          if str(id) in utl.tex_list:
            utl.tex_list = utl.tex_list.replace(str(id), '')
          else:
            utl.tex_list += str(id) + ' '
          print(utl.tex_list)
          utl.save()
        except:
          new_utl = UserTexList(username = name, tex_list = str(id))
          new_utl.save()

  context = {
    'title': 'Задача',
    'is_admin': request.user.groups.filter(name='admin').exists(),
    'problem': task(id),
  }

  return render(request, 'pages/problem.html', context)

def search(request):

  try:
    req = request.GET['req']
  except:
    req = '!`-'

  context = {
    'title': 'Поиск',
    'is_admin': request.user.groups.filter(name='admin').exists(),
    'task_list': search_database(req),
    'req': req,
  }

  return render(request, 'pages/search.html', context)


def p404(request, *args, **kwargs):
  return render(request, 'pages/404.html', {'title': 'Ошибка'})