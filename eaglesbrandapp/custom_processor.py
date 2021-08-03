from eaglesbrandapp.models import *

def footer_service(request):
    services = Services.objects.order_by('-created')
    return {'services':services}