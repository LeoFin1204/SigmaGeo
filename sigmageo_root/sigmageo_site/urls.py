from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url = '/static/images/favicon.ico', permanent = True)),
    path('sigma_geo/latex/', include('latex.urls')),
    path('sigma_geo/editing/', include('editing.urls')),
    path('sigma_geo/feedback/', include('feedback.urls')),
    path('sigma_geo/auth/', include('login.urls')),
    path('sigma_geo/', include('collection.urls')),
    path('', include('pages.urls')),
]
