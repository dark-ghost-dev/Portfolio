from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, ProjectSitemap
from . import views

sitemaps = {
    'static': StaticSitemap,
    'projects': ProjectSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('robots.txt', views.robots_txt, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]