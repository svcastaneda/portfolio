from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home), 
    # name='accomplishment_list'),
    url(r'^projects', views.projects),
    url(r'^resume', views.resume),
    url(r'^contact', views.contact)
]