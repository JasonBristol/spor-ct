from django.conf.urls import url

from . import views
import search.views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/(?P<slug>[\w-]+)', views.blog_post, name='post-detail'),
    url(r'^posts/(?P<year>[0-9]{4})/$', views.year_archive, name='posts-year-archive'),
    url(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='posts-month-archive'),
    url(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.day_archive, name='posts-day-archive'),
    url(r'^category/(?P<category>[\w-]+)', views.post_category, name="post-category"),
    url(r'^tag/(?P<tag>[\w-]+)', views.post_tag, name="post-tag"),
    url(r'^search/', search.views.search),
    url(r'^search/(?P<slug>[\w-]+)', search.views.search_blog, name="search-blog"),
]
