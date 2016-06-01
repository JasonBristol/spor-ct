from django.shortcuts import render, get_object_or_404
from .models import Case
from itertools import chain
from operator import attrgetter

def index(request):
    cases = Case.objects.filter(public=True)
    return render(request, 'investigations/index.html', {'cases': cases})

def case(request, slug):
    case = get_object_or_404(Case, slug=slug)
    related_cases = case.related_cases.filter(public=True)
    team_members = case.present_team_members.all()
    guests = case.present_guests.all()

    parties_present = sorted(chain(team_members, guests), key=attrgetter('last_name'))

    return render(request, 'investigations/case.html', {
        'case': case,
        'related_cases': related_cases,
        'parties_present': parties_present
    })