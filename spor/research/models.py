from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User)
    thumbnail = models.ImageField(upload_to="research/img")
    thumbnail_200x100 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(200, 100)], format='PNG', options={'quality': 100})
    thumbnail_500x300 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(500, 300)], format='PNG', options={'quality': 100})
    thumbnail_700x400 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(700, 400)], format='PNG', options={'quality': 100})
    thumbnail_750x500 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(750, 500)], format='PNG', options={'quality': 100})
    document = models.FileField(upload_to="research/{0}/".format(1), blank=True)
    date_published = models.DateTimeField(auto_now=True)
    related_projects = models.ManyToManyField('self', blank=True)
    publish = models.BooleanField(default=False)

    slug = models.SlugField(unique=True, help_text="Only change this if you know what you are doing")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kw):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kw)
