from home.models import Banner, Alert, Modal
from django.conf import settings

def get_banners(request):
  	banners = Banner.objects.all()
  	context = {}
  	context['banners'] = banners or None
  	return context

def get_alerts(request):
	site_alerts = Alert.objects.all()
	context = {}
	context['site_alerts'] = site_alerts
	return context

def get_modals(request):
	modals = Modal.objects.all()
	context = {}
	context['modals'] = modals
	return context

def get_custom_settings(request):
	context = {}
	context['fb_app_id'] = settings.FB_APP_ID
	return context