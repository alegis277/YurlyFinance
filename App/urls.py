from django.urls import path
from django.urls import include, re_path
from django.views.generic.base import RedirectView
from django.templatetags.static import static

favicon_view = RedirectView.as_view(url=static('favicon.png'), permanent=True)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', favicon_view, name='favicon'),
]