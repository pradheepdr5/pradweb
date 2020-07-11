from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bio, WorkAcademics, Accomplishment, Project

def home(request):
    try:
        bio = Bio.objects.all().order_by('-id')[0]
        experience = WorkAcademics.objects.all().order_by('-id')[0]
        accomplishments = Accomplishment.objects.all().order_by('-id').filter(is_published=True)
        projects = Project.objects.all().order_by('-id').filter(is_published=True)

        context = {
        'bio': bio,
        'experience': experience,
        'accomplishments': accomplishments,
        'projects' : projects
        }
        
    except IndexError:
        print("Index Error")
    else:
        return render(request, 'index/base.html', context)
    

  
    
