from django import template
from eaglesbrandapp.models import *

register = template.Library()

@register.inclusion_tag('eaglesbrandapp/include/latest-post.html')
def latest_post():
    posts = BlogPost.objects.order_by('-created')
    return {'most_recent':posts}

@register.inclusion_tag('eaglesbrandapp/include/partners-pic.html')
def partner_pic():
    partner = Partner.objects.order_by('-created')
    return {'partner':partner}

