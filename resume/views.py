from django.shortcuts import render
from .forms import send_email
from .models import Accomplishment, Skill, Project, Experience, School, Activity

# Create your views here.

def home(request):
    return render(request, 'mysite/blah.html')

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
    
def sent(request):
    if request.method=='POST':
        form = send_email(request.POST)
        
        if form.is_valid():
            sender = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            return HttpResponseRedirect('/')
    else:
        form = send_email()
    
    return render(request, 'mysite/projects.html', {'form':form})