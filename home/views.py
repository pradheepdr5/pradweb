from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bio, WorkAcademics, Accomplishment, Project, Portfolio, Contact

def home(request):
    try:
        bio = Bio.objects.all().order_by('-id')[0]
        experience = WorkAcademics.objects.all().order_by('-id')[0]
        accomplishments = Accomplishment.objects.all().order_by('-id').filter(is_published=True)
        projects = Project.objects.all().order_by('-id').filter(is_published=True)
        portfolio = Portfolio.objects.all()[0]
        contact = Contact.objects.all().order_by('-id')[0]
        context = {
        'bio': bio,
        'experience': experience,
        'accomplishments': accomplishments,
        'projects' : projects,
        'portfolio' : portfolio,
        'contact' : contact,
        }
        
    except IndexError:
        print("Index Error")
    else:
        return render(request, 'index/index.html', context)
