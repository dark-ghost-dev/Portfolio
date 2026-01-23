from django.shortcuts import render
from .models import SocialUser

def home(request):
    social_users = SocialUser.objects.all()
    return render(request, 'core/home.html', {'social_users': social_users})