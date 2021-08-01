from django.contrib import admin
from django.utils.html import format_html
from eaglesbrandapp.models import *


# Register your models here.
admin.site.site_header = 'EAGLESBRAND SOLUTIONS'


@admin.register(About) 
class About(admin.ModelAdmin):

    def abt_img1(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.image1.url))

    abt_img1.short_description = 'About'

    list_display = ['abt_img1','title','created',]


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}
    def pst_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))
    pst_img.short_description = 'Blog Post'

    list_display = ['pst_title',  'pst_img', 'time', ]

@admin.register(Project)
class Project(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}
    def pst_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))

    pst_img.short_description = 'Project'
    list_display = ['pst_title', 'pst_img', 'created' ]


@admin.register(Services) 
class Services(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}

    def img_url(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))

    img_url.short_description = 'Service'
    list_display = ['pst_title', 'pst_image', 'created',]


@admin.register(Comment)
class Comment(admin.ModelAdmin):
   
    list_display = [
        'user_name',
        'timestamp',
        'post',
       
    ]
