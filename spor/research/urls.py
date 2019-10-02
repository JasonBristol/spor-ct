from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project/<slug>/', views.research_project, name="project-detail"),
]
