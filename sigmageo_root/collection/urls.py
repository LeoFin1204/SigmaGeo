from django.urls import path
from . import views

urlpatterns = [
  path('', views.main),
  path('problem', views.problem),
  path('search', views.search),
  path('<str:section>/', views.subsection),
  path('<str:section>', views.section),
]