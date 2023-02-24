from django.shortcuts import render
from app.models import *
from django.views.generic import ListView
# Create your views here.
class list_view(ListView):
    model=school
    context_object_name='school'
    template_name='app/list_view.html'
    ordering=['name']
