from __future__ import unicode_literals

from django.db import models

class TeamMember(models.Model):
    fname = models.CharField(max_length=50, verbose_name="First Name")
    lname = models.CharField(max_length=50, verbose_name="Last Name")
    title = models.CharField(max_length=50, default="Member")
    thumbnail = models.ImageField(upload_to="images/team", help_text="750x450 works the best")
    description = models.TextField()
    facebook = models.BooleanField(default=True)
    facebook_url = models.URLField(blank=True)
    twitter = models.BooleanField(default=True)
    twitter_url = models.URLField(blank=True)
    linkedin = models.BooleanField(default=True)
    lindedin_url = models.URLField(blank=True)

    def __unicode__(self):
        return "{fname} {lname}".format(fname=self.fname, lname=self.lname)

    class Meta:
        verbose_name="Team Member"

class Customer(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="images/customers", help_text="500x300 works the best")
    url = models.URLField(blank=True)

    def __unicode__(self):
        return "Customer: {name}".format(name=self.name)

class Contact(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    hours = models.CharField(max_length=255)
    facebook = models.BooleanField(default=True)
    facebook_url = models.URLField(blank=True)
    twitter = models.BooleanField(default=True)
    twitter_url = models.URLField(blank=True)
    linkedin = models.BooleanField(default=True)
    lindedin_url = models.URLField(blank=True)
    gplus = models.BooleanField(default=True)
    gplus_url = models.URLField(blank=True)

    def __unicode__(self):
        return "{address} {city}, {state} {zipcode}".format(
            address=self.address,
            city=self.city,
            state=self.state,
            zipcode=self.zipcode
        )

class Banner(models.Model):
    image = models.ImageField(upload_to="images/banners")
    caption = models.CharField(max_length=25)

    def __unicode__(self):
        return self.caption

class Alert(models.Model):
    SEVERITY = (
        ("info", "Info"),
        ("warning", "Warning"),
        ("success", "Good"),
        ("danger", "Bad")
    )

    severity = models.CharField(max_length=10, choices=SEVERITY, default="info")
    header = models.CharField(max_length=25)
    body = models.TextField()
    dismissable = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.header
        
class Modal(models.Model):
    SEVERITY = (
        ("default", "Default"),
        ("info", "Info"),
        ("warning", "Warning"),
        ("success", "Good"),
        ("danger", "Bad")
    )

    severity = models.CharField(max_length=10, choices=SEVERITY, default="default")
    header = models.CharField(max_length=25)
    body = models.TextField(help_text="You can enter HTML or any other markup in here that needs to be rendered")
    popup = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.header