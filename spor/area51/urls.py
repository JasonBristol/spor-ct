from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^portfolio-1-col/$', views.portfolio_1_col),
    url(r'^portfolio-2-col/$', views.portfolio_2_col),
    url(r'^portfolio-3-col/$', views.portfolio_3_col),
    url(r'^portfolio-4-col/$', views.portfolio_4_col),
    url(r'^blog-home-2/$', views.blog_home_2),
    url(r'^full-width/$', views.full_width),
    url(r'^sidebar/$', views.sidebar),
    url(r'^404/$', views.four_o_four),
    url(r'^pricing/$', views.pricing),
]