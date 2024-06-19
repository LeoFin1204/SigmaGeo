from django.urls import path
from . import views

urlpatterns = [
  path('add_task', views.add_task),
  path('edit_task', views.redact_task),
  path('add_section', views.add_section),
  path('edit_section', views.redact_section),
  path('<str:a>', views.p404),
]