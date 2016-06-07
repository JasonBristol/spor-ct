from __future__ import unicode_literals

from django.db import models
from home.models import TeamMember, Contact
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
import os


class AudioEvidence(models.Model):
    label = models.CharField(max_length=50)
    file = models.FileField(upload_to="investigation/{0}/audio".format(1))
    details = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Audio Evidence"

    def __unicode__(self):
        return self.label

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        if extension.lower() == '.mp3':
            return 'mpeg'
        if extension.lower() == '.ogg':
            return 'ogg'
        if extension.lower() == '.wav':
            return 'wav'
        return 'other'


class ImageEvidence(models.Model):
    label = models.CharField(max_length=50)
    file = models.ImageField(upload_to="investigation/{0}/image".format(1))
    details = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Image Evidence"

    def __unicode__(self):
        return self.label


class PersonalExperience(models.Model):
    label = models.CharField(max_length=50)
    file = models.FileField(upload_to="investigation/{0}/text".format(1), blank=True)
    details = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Personal Experiences"

    def __unicode__(self):
        return self.label


class VideoEvidence(models.Model):
    label = models.CharField(max_length=50)
    file = models.FileField(upload_to="investigation/{0}/video".format(1))
    details = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Video Evidence"

    def __unicode__(self):
        return self.label

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        if extension.lower() == '.mp4':
            return 'mp4'
        if extension.lower() in ['.ogg', '.ogv', '.ogm']:
            return 'ogg'
        if extension.lower() == '.webm':
            return 'webm'
        return 'other'


class MiscEvidence(models.Model):
    label = models.CharField(max_length=50)
    file = models.FileField(upload_to="investigation/{0}/misc".format(1), blank=True)
    details = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name_plural = "Misc Evidence"

    def __unicode__(self):
        return self.label


class GuestInvestigator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=255)

    def __unicode__(self):
        return "{fname} {lname}".format(fname=self.first_name, lname=self.last_name)


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
    location = models.ForeignKey(Contact)
    date_occured = models.DateTimeField(blank=True, null=True)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    present_team_members = models.ManyToManyField(TeamMember, blank=True)
    present_guests = models.ManyToManyField(GuestInvestigator, blank=True)
    evidence_repository = models.URLField(blank=True, null=True)
    image_evidence = models.ManyToManyField(ImageEvidence, blank=True)
    audio_evidence = models.ManyToManyField(AudioEvidence, blank=True)
    video_evidence = models.ManyToManyField(VideoEvidence, blank=True)
    misc_evidence = models.ManyToManyField(MiscEvidence, blank=True)
    personal_experiences = models.ManyToManyField(PersonalExperience, blank=True)
    conclusion = models.CharField(max_length=25, choices=CONCLUSIONS, default="indeterminate")
    status = models.CharField(max_length=25, choices=CASE_STATUSES, default="proposed")
    related_cases = models.ManyToManyField('self', blank=True)
    public = models.BooleanField(default=False)

    slug = models.SlugField(unique=True, help_text="Only change this if you know what you are doing")

    def __unicode__(self):
        return self.case_number

    def full_address(self):
        return str(self.location)

    def save(self, *args, **kw):
        self.slug = slugify(self.case_number)
        super(Case, self).save(*args, **kw)
