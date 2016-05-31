from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^case/(?P<slug>[\w-]+)', views.case, name="case-detail"),
]