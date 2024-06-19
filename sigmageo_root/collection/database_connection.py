import sqlite3
import ast
from .models import Problem, Olimp, Book, Theme

TASK_PER_PAGE = 15
SECTION = {
  'olimps': Olimp,
  'books': Book,
  'themes': Theme,
}


def all_subsection(section):
  a = SECTION[section].objects.all()
  return [i.name for i in a]


def subsection_tasks(subsection, page):
  a = Problem.objects.filter(source = subsection)
  if (page-1) * TASK_PER_PAGE >= len(a):
    return list()
  a = a[TASK_PER_PAGE*(page-1):min(TASK_PER_PAGE*page, len(a))]
  for i in range(len(a)):
    a[i].themes = ast.literal_eval(a[i].themes)
  return a


def task(id):
  a = Problem.objects.get(id = id)
  a.themes = ast.literal_eval(a.themes)
  return a


def search_database(req, params = ('text', 'solution',)):
  a = Problem.objects.filter(text__icontains=req) | Problem.objects.filter(solution__icontains=req)
  for i in range(len(a)):
    a[i].themes = ast.literal_eval(a[i].themes)
  return a


def last_page(subsection):
  a = Problem.objects.filter(source = subsection)
  return (len(a)-1) // TASK_PER_PAGE + 1

