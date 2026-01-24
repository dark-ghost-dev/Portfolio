from django.shortcuts import render
from .models import SocialUser

def home(request):
    social_users = SocialUser.objects.filter(active=True)
    social_users_in_footer = social_users.filter(is_in_footer=True)
    return render(request, 'core/home.html', {'social_users': social_users, 'social_users_in_footer': social_users_in_footer})