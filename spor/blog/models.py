from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from django.urls import reverse

import itertools


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = "categories"


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, default="Blog Post")
    tagline = models.CharField(max_length=100)
    body = models.TextField(help_text="You can include HTML markup in the post body")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField(upload_to="images/posts", blank=True, help_text="900x300 works the best")
    thumbnail_900x300 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(900, 300)], format='PNG', options={'quality': 100})
    thumbnail_200x100 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(200, 100)], format='PNG', options={'quality': 100})
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='d')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True, help_text="Only change this if you know what you are doing")

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

    def __unicode__(self):
        return "{title} by {author}".format(
            title=self.title,
            author=self.author
        )

    def save(self, *args, **kw):
        max_length = 25
        self.slug = orig = slugify(self.title)[:max_length]
        for x in itertools.count(1):
            if not Post.objects.filter(slug=self.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
        super(Post, self).save(*args, **kw)
