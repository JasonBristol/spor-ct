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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
import home.views

urlpatterns = [
    path('about/', home.views.about),
    path('help/', home.views.help_page),
    path('events/', include('events.urls')),
    path('investigations/', include('investigations.urls')),
    path('research/', include('research.urls')),
    path('blog/', include('blog.urls')),
    path('services/', home.views.services),
    path('contact/', home.views.contact_page),
    path('area51/', include('area51.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', home.views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
