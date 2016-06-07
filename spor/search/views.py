from .utils import generic_search
from blog.models import Post, Category, Tag
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def search(request):
    if request.method == 'POST':
        slug = request.POST.get('search_term', None)

        if slug is not None:
            return reverse('search_blog', args=(slug))

    return redirect("/blog/")


def search_blog(request, slug):
    query = "search-query"

    MODEL_MAP = {
        Post: ["title", "tagline", "body", "author", "category", "tags"],
        Category: ["name"],
        Tag: ["name"],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render(request, "blog/search_results.html", {
        "objects": objects,
        "search_string": request.GET.get(query, ""),
    })
