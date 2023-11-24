from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class PictureView(ListView):
    model = Picture
    template_name = 'home.html'
    context_object_name = 'one1'