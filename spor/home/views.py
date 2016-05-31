from django.shortcuts import render
from django.template import RequestContext

from .models import TeamMember, Customer, Contact


def index(request):
    return render(request, 'home/index.html')

def about(request):
    team_members = TeamMember.objects.all()
    customers = Customer.objects.all()
    return render(request, 'home/about.html', {'team_members': team_members, 'customers': customers})

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'home/contact.html', {'contacts': contacts})