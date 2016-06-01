from django.shortcuts import render
from django.template import RequestContext

from .models import TeamMember, Partner, Contact


def index(request):
    return render(request, 'home/index.html')

def about(request):
    team_members = TeamMember.objects.all()
    partners = Partner.objects.all()
    return render(request, 'home/about.html', {'team_members': team_members, 'partners': partners})

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    contact = Contact.objects.get(primary_contact=True)
    return render(request, 'home/contact.html', {'contact': contact})