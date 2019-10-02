from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('case/<slug>/', views.investigation_case, name="case-detail"),
]
