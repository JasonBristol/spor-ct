from django.urls import path

from . import views

urlpatterns = [
    path('portfolio-1-col/', views.portfolio_1_col),
    path('portfolio-2-col/', views.portfolio_2_col),
    path('portfolio-3-col/', views.portfolio_3_col),
    path('portfolio-4-col/', views.portfolio_4_col),
    path('blog-home-2/', views.blog_home_2),
    path('full-width/', views.full_width),
    path('sidebar/', views.sidebar),
    path('404/', views.four_o_four),
    path('pricing/', views.pricing),
]
