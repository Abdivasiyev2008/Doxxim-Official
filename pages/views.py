from django.shortcuts import render
from django.views.generic import *


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
