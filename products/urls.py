from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('forms.py', views.new),
    path('postit',views.postit)
]