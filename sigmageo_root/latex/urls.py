from django.urls import path
from . import views

urlpatterns = [
  path('', views.task_list),
  path('compile', views.compile),
  path('<str:a>', views.p404),
]