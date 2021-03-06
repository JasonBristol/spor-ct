from django.contrib import admin
from .models import TeamMember, Partner, Contact, Banner, Alert, Modal
from django.core.validators import EMPTY_VALUES
from django import forms


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def clean(self):
        facebook = self.cleaned_data.get('facebook', False)
        linkedin = self.cleaned_data.get('linkedin', False)
        twitter = self.cleaned_data.get('twitter', False)

        if facebook:
            facebook_url = self.cleaned_data.get('facebook_url', None)
            if facebook_url in EMPTY_VALUES:
                self._errors['facebook_url'] = self.error_class([
                    'A URL is required if this team member has a Facebook page'])

        if linkedin:
            linkedin_url = self.cleaned_data.get('linkedin_url', None)
            if linkedin_url in EMPTY_VALUES:
                self._errors['linkedin_url'] = self.error_class([
                    'A URL is required if this team member has a Linkedin page'])

        if twitter:
            twitter_url = self.cleaned_data.get('twitter_url', None)
            if twitter_url in EMPTY_VALUES:
                self._errors['twitter_url'] = self.error_class([
                    'A URL is required if this team member has a Twitter page'])

        return self.cleaned_data


class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberForm

admin.site.register(TeamMember, TeamMemberAdmin)


class PartnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partner, PartnerAdmin)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def clean(self):
        facebook = self.cleaned_data.get('facebook', False)
        linkedin = self.cleaned_data.get('linkedin', False)
        twitter = self.cleaned_data.get('twitter', False)
        gplus = self.cleaned_data.get('gplus', False)

        if facebook:
            facebook_url = self.cleaned_data.get('facebook_url', None)
            if facebook_url in EMPTY_VALUES:
                self._errors['facebook_url'] = self.error_class([
                    'A URL is required if this contact has a Facebook page'])

        if linkedin:
            linkedin_url = self.cleaned_data.get('linkedin_url', None)
            if linkedin_url in EMPTY_VALUES:
                self._errors['linkedin_url'] = self.error_class([
                    'A URL is required if this contact has a Linkedin page'])

        if twitter:
            twitter_url = self.cleaned_data.get('twitter_url', None)
            if twitter_url in EMPTY_VALUES:
                self._errors['twitter_url'] = self.error_class([
                    'A URL is required if this contact has a Twitter page'])

        if gplus:
            gplus_url = self.cleaned_data.get('gplus_url', None)
            if gplus_url in EMPTY_VALUES:
                self._errors['gplus_url'] = self.error_class([
                    'A URL is required if this contact has a Google+ page'])

        return self.cleaned_data


class ContactAdmin(admin.ModelAdmin):
    form = ContactForm

admin.site.register(Contact, ContactAdmin)


class BannerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Banner, BannerAdmin)


class AlertAdmin(admin.ModelAdmin):
    pass

admin.site.register(Alert, AlertAdmin)


class ModalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Modal, ModalAdmin)
