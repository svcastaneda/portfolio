from django.contrib import admin
from .models import School, Skill, Experience, Accomplishment, Activity, Project

# Register your models here.

admin.site.register([School, Skill, Experience, Accomplishment, Activity, Project])