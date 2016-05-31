from django.shortcuts import render
from django.template import RequestContext

from .models import FAQ, KnownIssue, BugCategory


def index(request):
    faqs = FAQ.objects.all()
    issues = KnownIssue.objects.all()
    categories = BugCategory.objects.order_by('name')

    return render(request, 'helper/index.html', {'faqs': faqs, 'issues': issues, 'categories': categories})