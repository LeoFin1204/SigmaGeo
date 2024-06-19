from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.contrib.auth import login, authenticate, logout

def home(request):

  context = {
    'title': 'Домашняя страница',
    'is_admin': request.user.groups.filter(name='admin').exists()
  }

  return render(request, 'pages/home.html', context)

def about(request):

  context = {
    'title': 'О нас',
    'is_admin': request.user.groups.filter(name='admin').exists()
  }

  return render(request, 'pages/about.html', context)

def p404(request, *args, **kwargs):
  return (request, 'pages/404.html', {'title': 'Ошибка'})