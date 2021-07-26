from django.contrib import admin
from django.utils.html import format_html
from eaglesbrandapp.models import *


# Register your models here.
admin.site.site_header = 'VITONIA LEAD FOUNDATION'
admin.site.register(Comment)


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}
    # def post_img(self, obj):
    #     return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))
    # post_img.short_description = 'Blog Post'
    
    def post_content(self, obj):
        return obj.content[:50]
    list_display = ['pst_title',  'post_content', 'time', ]

@admin.register(Project)
class Project(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}
    def img_url(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))

    img_url.short_description = 'Blog Post'
    list_display = ['pst_title', 'pst_image',  'time', 'created' ]


@admin.register(Services) 
class Services(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pst_title',)}

    def img_url(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.pst_image.url))

    img_url.short_description = 'Service'
    list_display = ['pst_title', 'pst_image', 'created',]
