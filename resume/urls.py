from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.accomplishment_list, name='accomplishment_list'),
]