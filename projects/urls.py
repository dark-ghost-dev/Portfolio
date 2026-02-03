from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<slug:project_slug>/', views.project, name='project'),
]