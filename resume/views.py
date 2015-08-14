from django.shortcuts import render
from .models import Accomplishment

# Create your views here.

def accomplishment_list(request):
    accomplishments = Accomplishment.objects.all()
    return render(request, 'resume/accomplishment_list.html', {})