from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag


def index(request):
    blog_posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat_1 = categories[len(categories)/2:]
    cat_2 = categories[:len(categories)/2]

    return render(request, 'blog/index.html', {
        'blog_posts': blog_posts,
        'tags': tags,
        'categories': categories,
        'cat_1': cat_1,
        'cat_2': cat_2
    })


def blog_post(request, slug):
    import datetime

    post = get_object_or_404(Post, slug=slug)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat_1 = categories[len(categories) / 2:]
    cat_2 = categories[:len(categories) / 2]

    edited = abs(post.date_created - post.date_modified) > datetime.timedelta(seconds=1)

    return render(request, 'blog/post.html', {
        'post': post,
        'edited': edited,
        'tags': tags,
        'categories': categories,
        'cat_1': cat_1,
        'cat_2': cat_2
    })


def year_archive(request, year):
    pass


def month_archive(request, year, month):
    pass


def day_archive(request, year, month, day):
    pass


def post_category(request, category):
    blog_posts = Post.objects.filter(category__name=category)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat_1 = categories[len(categories) / 2:]
    cat_2 = categories[:len(categories) / 2]

    return render(request, 'blog/index.html', {
        'blog_posts': blog_posts,
        'tags': tags,
        'categories': categories,
        'cat_1': cat_1,
        'cat_2': cat_2
    })


def post_tag(request, tag):
    blog_posts = Post.objects.filter(tags__name=tag)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat_1 = categories[len(categories) / 2:]
    cat_2 = categories[:len(categories) / 2]

    return render(request, 'blog/index.html', {
        'blog_posts': blog_posts,
        'tags': tags,
        'categories': categories,
        'cat_1': cat_1,
        'cat_2': cat_2
    })
