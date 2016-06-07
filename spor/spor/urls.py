"""spor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
import home.views

urlpatterns = [
    url(r'^about/', home.views.about),
    url(r'^events/', include('events.urls')),
    url(r'^investigations/', include('investigations.urls')),
    url(r'^research/', include('research.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^services/', home.views.services),
    url(r'^contact/', home.views.contact),
    url(r'^help/', include('helper.urls')),
    url(r'^area51/', include('area51.urls')),
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^$', home.views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
