from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'research/index.html', {'projects': projects})

def project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    return render(request, 'research/project.html', {
        'project': project
    })