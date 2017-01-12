from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    """
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta(object):
        abstract = True


class UserProfile(BaseModel):
    """
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{fname} {lname}".format(
            fname=self.user.first_name,
            lname=self.user.last_name
        )

    def full_name(self):
        return "{fname} {lname}".format(
            fname=self.user.first_name,
            lname=self.user.last_name
        )


class FAQ(BaseModel):
    """
    """
    question = models.CharField(max_length=255, help_text="Plain text or HTML input is accepted.")
    answer = models.TextField(help_text="Plain text or HTML input is accepted.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question

    class Meta(object):
        verbose_name = "FAQ"


class BugCategory(BaseModel):
    """
    """
    name = models.CharField(max_length=25)
    value = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = "Bug Categories"


class BugReport(BaseModel):
    """
    """
    # Make these integer based
    BUG_SEVERITY = (
        ("none", "Non-Issue"),
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    )

    BUG_STATUS = (
        ("review", "Review"),
        ("scheduled_fix", "Scheduled Fix"),
        ("in_progress", "In Progress"),
        ("fixed", "Fixed"),
        ("closed", "Closed"),
        ("blocked", "Blocked"),
    )

    category = models.ForeignKey(BugCategory, on_delete=models.PROTECT)
    description = models.TextField()
    severity = models.CharField(max_length=25, choices=BUG_SEVERITY, default="low")
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=25, choices=BUG_STATUS, default="review")
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{name} - {date}".format(
            name=self.category.name,
            date=self.date_submitted
        )

    class Meta(object):
        verbose_name = "Bug Report"


class KnownIssue(BaseModel):
    """
    """
    tagline = models.CharField(max_length=255, help_text="Plain text or HTML input is accepted.")
    reference_bug = models.ForeignKey(BugReport, blank=True, null=True, on_delete=models.PROTECT)
    description = models.TextField(help_text="Plain text or HTML input is accepted.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.tagline

    class Meta(object):
        verbose_name = "Known Issue"



class TeamMember(BaseModel):
    """
    """
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    title = models.CharField(max_length=50, default="Member")
    thumbnail = models.ImageField(upload_to="images/team", help_text="750x450 works the best")
    description = models.TextField()
    date_joined = models.DateField(blank=True)
    facebook = models.BooleanField(default=False)
    facebook_url = models.URLField(blank=True)
    twitter = models.BooleanField(default=False)
    twitter_url = models.URLField(blank=True)
    linkedin = models.BooleanField(default=False)
    linkedin_url = models.URLField(blank=True)

    def __unicode__(self):
        return "{fname} {lname}".format(fname=self.first_name, lname=self.last_name)

    class Meta(object):
        verbose_name = "Team Member"


class Partner(BaseModel):
    """
    """
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="images/customers", help_text="500x300 works the best")
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Contact(BaseModel):
    """
    """
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    hours = models.CharField(max_length=255)
    google_map_url = models.CharField(max_length=255, blank=True, null=True, help_text="You can override the provided value, or set it blank to regenerate it")
    facebook = models.BooleanField(default=False)
    facebook_url = models.URLField(blank=True)
    twitter = models.BooleanField(default=False)
    twitter_url = models.URLField(blank=True)
    linkedin = models.BooleanField(default=False)
    linkedin_url = models.URLField(blank=True)
    gplus = models.BooleanField(default=False)
    gplus_url = models.URLField(blank=True)
    primary_contact = models.BooleanField(default=False, help_text="Primary contacts will show up on our contact page")

    def __unicode__(self):
        return "{address} {city}, {state} {zipcode}".format(
            address=self.address,
            city=self.city,
            state=self.state,
            zipcode=self.zipcode
        )

    def save(self, *args, **kw):
        if not self.google_map_url:
            from django.conf import settings
            uri = "{address},{city}+{state}".format(address=self.address.replace(" ", "+"), city=self.city, state=self.state)
            self.google_map_url = "https://www.google.com/maps/embed/v1/place?key={key}&q={uri}".format(key=settings.GOOGLE_MAPS_EMBED_API_KEY, uri=uri)
        super(Contact, self).save(*args, **kw)


class Banner(BaseModel):
    """
    """
    image = models.ImageField(upload_to="images/banners")
    caption = models.CharField(max_length=25)

    def __unicode__(self):
        return self.caption


class Alert(BaseModel):
    """
    """
    SEVERITY = (
        ("info", "Info"),
        ("warning", "Warning"),
        ("success", "Good"),
        ("danger", "Bad")
    )

    severity = models.CharField(max_length=10, choices=SEVERITY, default="info")
    header = models.CharField(max_length=25, help_text="Plain text or HTML input is accepted.")
    body = models.TextField(help_text="Plain text or HTML input is accepted.")
    dismissable = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.header


class Modal(BaseModel):
    """
    """
    SEVERITY = (
        ("default", "Default"),
        ("info", "Info"),
        ("warning", "Warning"),
        ("success", "Good"),
        ("danger", "Bad")
    )

    severity = models.CharField(max_length=10, choices=SEVERITY, default="default")
    header = models.CharField(max_length=25)
    body = models.TextField(help_text="Plain text or HTML input is accepted.")
    popup = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.header
