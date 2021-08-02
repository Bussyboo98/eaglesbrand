from eaglesbrandapp.models import *

def footer_service(request):
    service = Services.objects.order_by('-created')
    return {'service':service}