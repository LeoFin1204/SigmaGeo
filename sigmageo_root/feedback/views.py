from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

def feedback(request):

  context = {
    'title': 'Обратная связь',
    'is_admin': request.user.groups.filter(name='admin').exists()
  }

  return render(request, 'pages/feedback.html', context)