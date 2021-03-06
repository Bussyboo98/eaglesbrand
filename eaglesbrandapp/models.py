from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import reverse
from tinymce import HTMLField
from fontawesome_5.fields import IconField
import datetime


# Create your models here.


class BlogPost(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    slug = models.SlugField(unique=True)
    pst_image = ImageField('Post Image', upload_to='uploads/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Posted By')
    content = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, verbose_name='Posted By')
    pst_image1 = ImageField('Author Image', upload_to='uploads/', blank=True, null=True)
    content1 = models.TextField(verbose_name='Blog Summary', max_length=300,)
    today = datetime.date.today()
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    current_month = months[today.month]

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Blog Post'

    @property
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url
    def img1_url(self):
        if self.pst_image1:
            return self.pst_image1.url
    
    @property
    def get_comments(self):
        return self.comments.all()

    def get_post_url(self):
        return reverse('eaglesbrandapp:blog_detail', kwargs={
            'slug': self.slug,
        })
 
class Comment(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, verbose_name= 'User Name')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(verbose_name= 'Content')
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name


class About(models.Model):
    title = models.CharField(max_length=50)
    abt_content = HTMLField('Content')
    image1 = models.FileField(null=True, blank=True, upload_to='uploads/')
    our_vision = models.TextField(verbose_name='Our Vision', blank=True, null=True)
    our_mission = models.TextField(verbose_name='Our Mission', blank=True, null=True)
    our_value = models.TextField(verbose_name='Our Values', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural='About'

    def abt_img1(self):
        if self.image1:
            return self.image1.url

class Project(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='Project Title')
    slug = models.SlugField(unique=True)
    pst_image = ImageField('Project Image', upload_to='uploads/', blank=True, null=True)
    content = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Project'

    @property
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url
   

    def get_project_url(self):
        return reverse('eaglesbrandapp:project_detail', kwargs={
            'slug': self.slug,
        })
 
class Services(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name= 'Service Title')
    slug = models.SlugField()
    icon = IconField()
    pst_image = ImageField('Service Image', upload_to='uploads/', blank=True, null=True)
    content = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pst_title

    @property
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url
   

    def get_service_url(self):
        return reverse('eaglesbrandapp:service_detail',kwargs={'slug':self.slug,})
    class Meta():
        verbose_name_plural = 'Services'



class HomeSlider(models.Model):
    slide_text = models.CharField(blank=True, null=True, max_length=100)
    slide_content1 = models.TextField(blank=True, null=True)
    slide_content2 = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slide_text
    

    class Meta():
        verbose_name_plural = 'Home Slider'

class Partner(models.Model):
    image1 = models.FileField(null=True, blank=True, upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name_plural='Partner'
    @property
    def pat_img1(self):
        if self.image1:
            return self.image1.url


class Team(models.Model):
    image = models.FileField(null=True, blank=True, upload_to='uploads/')
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name_plural='Team'
    @property
    def team_img(self):
        if self.image:
            return self.image.url

    def __str__(self):
        return self.name
