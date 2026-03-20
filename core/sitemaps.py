from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from projects.models import Project


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return ['home']

    def location(self, obj):
        return reverse(obj)


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Project.objects.filter(active=True)
    
    def location(self, obj):
        return f"/projects/{obj.slug}/"

    def lastmod(self, obj):
        return obj.modified