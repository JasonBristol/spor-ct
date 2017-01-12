from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import FAQ, KnownIssue, TeamMember, Partner, Contact
from .forms import BugReportForm


def index(request):
    return render(request, 'home/index.html')


def about(request):
    team_members = TeamMember.objects.all()
    partners = Partner.objects.all()
    return render(request, 'home/about.html', {'team_members': team_members, 'partners': partners})


def services(request):
    return render(request, 'home/services.html')

def help_page(request):
    """
    """
    faqs = FAQ.objects.all()
    issues = KnownIssue.objects.exclude(reference_bug__status__in=["Fixed", "Closed"])

    if request.method == 'POST':
        form = BugReportForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, """
                <div class="alert alert-success" role="alert">
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <i class="fa fa-check-circle" aria-hidden="true"></i> <strong>Bug Rreport submitted!</strong> Thank you for your feedback!
                </div>
            """)
            return HttpResponseRedirect('/help/')
    else:
        form = BugReportForm()

    return render(request, 'home/help.html', {'faqs': faqs, 'issues': issues, 'form': form})


def contact_page(request):
    contact = Contact.objects.get(primary_contact=True)
    return render(request, 'home/contact.html', {'contact': contact})
