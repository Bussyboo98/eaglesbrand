from django.urls import path
from eaglesbrandapp import views

app_name = 'eaglesbrandapp'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('blog-page/', views.blog, name='blog'),
    path('contact-page/', views.contact, name='contact'),
    path('services-page/', views.services, name='services'),
    
]
