from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^project/(?P<slug>[\w-]+)', views.research_project, name="project-detail"),
]
