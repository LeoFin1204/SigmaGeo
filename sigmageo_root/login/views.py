from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def registration(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')

      user = authenticate(username = username, password = password)
      login(request, user)
      return redirect('/')
  
  else:
    form = SignUpForm()

  return render(request, 'pages/registration.html', {'form' : form,})

def login_req(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    username = request.POST.get('username')
    password = request.POST.get('password1')

    try:
      user = authenticate(username = username, password = password)
      login(request, user)
      return redirect('/')
    except:
      pass
  
  else:
    form = LoginForm()

  return render(request, 'pages/login.html', {'form' : form,})

def logout_req(request):
  logout(request)

  return redirect('/')

def p404(request, *args, **kwargs):
  return render(request, 'pages/404.html', {'title': 'Ошибка'})