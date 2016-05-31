from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify

class Case(models.Model):
    CONCLUSIONS = (
        ("indeterminate", "Indeterminate"),
        ("in_progress", "In-Progress"),
        ("no_activity", "No Activity"),
        ("inconclusive", "Inconclusive"),
        ("active", "Active"),
        ("haunted", "Haunted"),
        ("under_review", "Under Review"),
    )

    CASE_STATUSES = (
        ("proposed", "Proposed"),
        ("accepted", "Accepted"),
        ("planning", "Planning"),
        ("scheduled", "Scheduled"),
        ("in_progress", "In-Progress"),
        ("analysis", "Analysis"),
        ("debrief", "Debrief"),
        ("completed", "Completed"),
        ("review", "Review"),
        ("rescheduled", "Rescheduled"),
        ("cancelled", "Cancelled"),
        ("incomplete", "Incomplete")
    )
    case_number = models.CharField(max_length=10, default="SPOR-00000")
    name = models.CharField(max_length=25)
    case_manager = models.ForeignKey(User)
    thumbnail = models.ImageField(upload_to="investigations/img", blank=True)
    thumbnail_200x100 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(200, 100)], format='PNG', options={'quality': 100})
    thumbnail_500x300 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(500, 300)], format='PNG', options={'quality': 100})
    thumbnail_700x300 = ImageSpecField(source='thumbnail', processors=[ResizeToFill(700, 300)], format='PNG', options={'quality': 100})
    location = models.CharField(max_length=255) # Setup a panel
    google_map = models.CharField(max_length=255, blank=True, help_text="Please paste markup for an embeded <a href='https://www.google.com/maps'>Google Map</a>")
    date_occured = models.DateTimeField(blank=True)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    conclusion = models.CharField(max_length=25, choices=CONCLUSIONS, default="indeterminate")
    status = models.CharField(max_length=25, choices=CASE_STATUSES, default="proposed")
    related_cases = models.ManyToManyField('self', blank=True)
    public = models.BooleanField(default=False)

    slug = models.SlugField(unique=True, help_text="Only change this if you know what you are doing")

    def __unicode__(self):
        return self.case_number

    def save(self, *args, **kw):
        self.slug = slugify(self.case_number)
        super(Case, self).save(*args, **kw)

class AudioEvidence(models.Model):
    label = models.CharField(max_length=20)
    case = models.ForeignKey(Case)
    file = models.FileField(upload_to="investigation/{0}/audio".format(1))

    class Meta:
        verbose_name_plural = "audio Evidence"

class ImageEvidence(models.Model):
    label = models.CharField(max_length=20)
    case = models.ForeignKey(Case)
    file = models.FileField(upload_to="investigation/{0}/image".format(1))

    class Meta:
        verbose_name_plural = "image Evidence"

class PersonalExperience(models.Model):
    label = models.CharField(max_length=20)
    case = models.ForeignKey(Case)
    file = models.FileField(upload_to="investigation/{0}/text".format(1), blank=True)
    details = models.TextField()

    class Meta:
        verbose_name_plural = "personal Experiences"

class VideoEvidence(models.Model):
    label = models.CharField(max_length=20)
    case = models.ForeignKey(Case)
    file = models.FileField(upload_to="investigation/{0}/video".format(1))

    class Meta:
        verbose_name_plural = "video Evidence"

class MiscEvidence(models.Model):
    label = models.CharField(max_length=20)
    case = models.ForeignKey(Case)
    file = models.FileField(upload_to="investigation/{0}/misc".format(1), blank=True)
    details = models.TextField()

    class Meta:
        verbose_name_plural = "misc Evidence"

class GuestInvestigator(models.Model):
    pass