from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Project
from core.models import SocialUser

def projects(request):
    social_users_in_hero = SocialUser.objects.filter(active=True, is_in_hero=True)
    #return redirect('home')
    return render(request, 'projects/project.html', {'social_users_in_hero': social_users_in_hero})

def project(request, project_slug):
    social_users_in_hero = SocialUser.objects.filter(active=True, is_in_hero=True)
    project = get_object_or_404(Project, slug=project_slug, active=True)
    return render(request, 'projects/project.html', {'project': project, 'social_users_in_hero': social_users_in_hero})