from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from eaglesbrandapp.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages



# Create your views here.


def index(request):
    return render(request, 'eaglesbrandapp/index.html')

def about(request):
    return render(request, 'eaglesbrandapp/about.html')

def blog(request):
    return render(request, 'eaglesbrandapp/blog.html')

def contact(request):
    return render(request, 'eaglesbrandapp/contact.html')

def services(request):
    return render(request, 'eaglesbrandapp/services.html')

def projects(request):
    return render(request, 'eaglesbrandapp/projects.html')

def service_detail(request):
    return render(request, 'eaglesbrandapp/service-detail.html')

def project_detail(request):
    return render(request, 'eaglesbrandapp/project_detail.html')

