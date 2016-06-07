from home.models import Banner, Alert, Modal
from django.conf import settings


def get_extras(request):
    banners = Banner.objects.all()
    site_alerts = Alert.objects.all()
    modals = Modal.objects.all()
    context = {}
    context['current_uri'] = request.build_absolute_uri()
    context['banners'] = banners or None
    context['site_alerts'] = site_alerts
    context['modals'] = modals
    context['fb_app_id'] = settings.FB_APP_ID
    return context
