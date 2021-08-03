from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from eaglesbrandapp.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings
from django.contrib import messages
from django.db.models import Count, Q
from eaglesbrandapp.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    service_home = Services.objects.all()[:3]
    project_home = Project.objects.order_by('-created')[:4]
    blog = BlogPost.objects.order_by('-created')
    about = About.objects.all()
    home = HomeSlider.objects.all()
    context = {
        'service_home': service_home,
        'project_home': project_home,
        'blog': blog,
        'about':about,
        'hme':home,
    }
    return render(request, 'eaglesbrandapp/index.html', context)

def about(request):
    about_us = About.objects.all()
    return render(request, 'eaglesbrandapp/about.html',{'abt':about_us})

def blog(request):
    most_recent = BlogPost.objects.order_by('created')[:6]
    posts = BlogPost.objects.order_by('-created')
    paginated_filter = Paginator(posts, 5)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    context = {
        'person_page_obj': posts, 
        'most_recent': most_recent,
        'post':posts, 
        'most_recent':most_recent
    }
    context['person_page_obj'] = person_page_obj  
    person_page_obj = paginated_filter.get_page(page_number)
    return render(request, 'eaglesbrandapp/blog.html', context)

def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'Eaglesrand Solutions'
        context = {
            'firstname':firstname,
            'lastname':lastname,
            'phone':phone,
            'email':email,
            'message': message
        }
        html_message = render_to_string('eaglesbrandapp/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = settings.FROM_HOST
        send = mail.send_mail(subject, plain_message, from_email, 
                      settings.RECIEVER_MAIL, html_message=html_message, fail_silently=False)
        if send:
            messages.success(request, 'Email sent succesfully!')
        else:
            messages.error(request, 'Mail not sent! Please make sure you are connected to internet')

    return render(request, 'eaglesbrandapp/contact.html')

def services(request):
    service = Services.objects.all()
    return render(request, 'eaglesbrandapp/services.html', {'service':service})

def projects(request):
    project = Project.objects.order_by('-created')
    return render(request, 'eaglesbrandapp/projects.html', {'project':project})

def service_detail(request, slug):
    service_detail = Services.objects.get(slug=slug)
    return render(request, 'eaglesbrandapp/service-detail.html', {'service': service_detail})

def project_detail(request, slug):
    project_post = Project.objects.get(slug=slug)
    return render(request, 'eaglesbrandapp/project_detail.html', {'project': project_post})

def search(request):
    most_recent = BlogPost.objects.order_by('created')[:6]
    queryset = BlogPost.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(pst_title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'most_recent':most_recent
        
    }
    return render(request, 'eaglesbrandapp/search_results.html', context)

def blog_detail(request, pk):
    most_recent = BlogPost.objects.order_by('created')[:6]
    single_post = get_object_or_404(BlogPost,  pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-timestamp')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
            return redirect('eaglesbrandapp:blog_detail', pk=single_post.pk)
            single_post = {'form': form, 'most_recent': most_recent,}
    else:
        form = CommentForm()
    return render(request, 'eaglesbrandapp/blog_details.html', {'comm':comments, 'form':form,  'most_recent':most_recent, 'single':single_post, 'sipst':single_post})
 