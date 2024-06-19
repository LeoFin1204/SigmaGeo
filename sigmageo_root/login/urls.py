from django.urls import path
from . import views

urlpatterns = [
  path('login', views.login_req),
  path('logout', views.logout_req),
  path('registration', views.registration),
  path('<str:a>', views.p404),
]