from django.urls import path

from . import views
import search.views

urlpatterns = [
    path('', views.index),
    path('post/<slug>/', views.blog_post, name='post-detail'),
    path('posts/<year>/', views.year_archive, name='posts-year-archive'),
    path('posts/<year>/<month>/', views.month_archive, name='posts-month-archive'),
    path('posts/<year>/<month>/<day>/', views.day_archive, name='posts-day-archive'),
    path('category/<category>/', views.post_category, name="post-category"),
    path('tag/<tag>/', views.post_tag, name="post-tag"),
    path('search/', search.views.search),
    path('search/<slug>/', search.views.search_blog, name="search-blog"),
]
