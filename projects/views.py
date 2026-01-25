from django.shortcuts import render
from django.shortcuts import redirect
from core.models import SocialUser

def projects(request):
    social_users_in_hero = SocialUser.objects.filter(active=True, is_in_footer=True)
    #return redirect('home')
    return render(request, 'projects/project.html', {'social_users_in_footer': social_users_in_hero})