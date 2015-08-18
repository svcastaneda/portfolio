from django.db import models
from django.utils import timezone

class School(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    concentration = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50)
    graduation = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    note = models.TextField(blank=True)
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
        
class Skill(models.Model):
    author = models.ForeignKey('auth.User')
    skill = models.TextField()
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.skill
        
class Experience(models.Model):
    author = models.ForeignKey('auth.User')
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.company

class Accomplishment(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
        
class Activity(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.TextField()
    duration = models.CharField(max_length=50)
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
              
class Project(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    alt = models.CharField(max_length=50)
    pic = models.CharField(max_length=500)
    description = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.name