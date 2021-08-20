from django.urls import path
from eaglesbrandapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'eaglesbrandapp'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('blog-page/', views.blog, name='blog'),
    path('contact-page/', views.contact, name='contact'),
    path('services-page/', views.services, name='services'),
    path('projects-page/', views.projects, name='projects'),
    path('service_detail-page/<slug:slug>/', views.service_detail, name='service_detail'),
    path('project_detail-page/<slug:slug>/', views.project_detail, name='project_detail'),
    path('search-page/', views.search, name='search'),
    path('blog-slug/<slug:slug>/', views.blog_detail, name='blog_detail'),
    
]
