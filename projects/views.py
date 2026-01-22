from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def projects(request):
    #return redirect('home')
    return render(request, 'projects/project.html')