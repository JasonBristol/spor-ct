from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"

class BugCategory(models.Model):
    name = models.CharField(max_length=25)
    value = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Bug Categories"

class BugReport(models.Model):
    BUG_SEVERITY = (
        ("none", "Non-Issue"),
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical")
    )

    BUG_STATUS = (
        ("review", "Review"),
        ("scheduled_fix", "Scheduled Fix"),
        ("in_progress", "In-Progress"),
        ("fixed", "Fixed"),
        ("closed", "Closed"),
        ("blocked", "Blocked"),
    )
    category = models.ForeignKey(BugCategory, on_delete=models.PROTECT)
    description = models.TextField()
    severity = models.CharField(max_length=25, choices=BUG_SEVERITY, default="low")
    assignee = models.ForeignKey(User, null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=25, choices=BUG_STATUS, default="review")
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{name} - {date}".format(name=self.category.name, date=self.date_submitted) # Investigate a bug-id

    class Meta:
        verbose_name = "Bug Report"

class KnownIssue(models.Model):
    tagline = models.CharField(max_length=255)
    reference_bug = models.ForeignKey(BugReport, blank=True, null=True)
    description = models.TextField()

    def __unicode__(self):
        return self.tagline

    class Meta:
        verbose_name = "Known Issue"