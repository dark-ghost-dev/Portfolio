from django.shortcuts import render
from django.db.models import Prefetch
from .models import SkillCategory, Skill, SocialUser

def home(request):
    skill_categories = SkillCategory.objects.filter(active=True).prefetch_related(
        Prefetch(
            'skills',
            queryset=Skill.objects.filter(active=True).order_by('order')
        )
    )
    social_users = SocialUser.objects.filter(active=True)
    social_users_in_footer = social_users.filter(is_in_footer=True)
    return render(request, 'core/home.html', {
        'skill_categories': skill_categories,
        'social_users': social_users,
        'social_users_in_footer': social_users_in_footer
    })