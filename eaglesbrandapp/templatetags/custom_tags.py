from django import template
from eaglesbrandapp.models import *

register = template.Library()

@register.inclusion_tag('eaglesbrandapp/include/latest-post.html')
def latest_post():
    posts = BlogPost.objects.order_by('-created')
    return {'most_recent':posts}

