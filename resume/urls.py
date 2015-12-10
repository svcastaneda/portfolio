from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home), 
    url(r'^projects', views.projects),
    url(r'^resume', views.resume),
    url(r'^contact', views.contact),
    # url(r'^sent', views.sent)
]