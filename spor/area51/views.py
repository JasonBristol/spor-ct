from django.shortcuts import render
from django.template import RequestContext, loader

def portfolio_1_col(request):
    return render(request, 'area51/portfolio-1-col.html')

def portfolio_2_col(request):
    return render(request, 'area51/portfolio-2-col.html')

def portfolio_3_col(request):
    return render(request, 'area51/portfolio-3-col.html')

def portfolio_4_col(request):
    return render(request, 'area51/portfolio-4-col.html')

def blog_home_2(request):
    return render(request, 'area51/blog-home-2.html')

def full_width(request):
    return render(request, 'area51/full-width.html')

def sidebar(request):
    return render(request, 'area51/sidebar.html')

def four_o_four(request):
    return render(request, 'home/404.html')

def pricing(request):
    return render(request, 'area51/pricing.html')