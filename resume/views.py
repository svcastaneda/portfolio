from django.shortcuts import render
from .models import Accomplishment, Skill, Project, Experience, School, Activity

# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

def resume(request):
    schools = School.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('created_date')
    accomplishments = Accomplishment.objects.all().order_by('created_date')
    activities = Activity.objects.all().order_by('created_date')
    divider = skills.count()/2
    
    return render(request, 'mysite/resume.html', {'schools':schools, 'experiences': experiences, 'accomplishments': accomplishments, 'activities': activities, 'skills_1': skills[:divider], 'skills_2': skills[divider::]})
    
def projects(request):
    projects = Project.objects.all().order_by('created_date')
    return render(request, 'mysite/projects.html', {'projects': projects})
    
def contact(request):
    return render(request, 'mysite/contact.html')