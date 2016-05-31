from django.shortcuts import render, get_object_or_404
from .models import Case

def index(request):
    cases = Case.objects.all()
    return render(request, 'investigations/index.html', {'cases': cases})

def case(request, slug):
    case = get_object_or_404(Case, slug=slug)

    return render(request, 'investigations/case.html', {
        'case': case
    })