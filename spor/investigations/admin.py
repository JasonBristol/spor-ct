from django.contrib import admin

from .models import Case, AudioEvidence, ImageEvidence, PersonalExperience, VideoEvidence, MiscEvidence, GuestInvestigator
from imagekit.admin import AdminThumbnail


class CaseAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'case_number', 'case_manager', 'slug', 'date_occured', 'status', 'conclusion')
    admin_thumbnail = AdminThumbnail(image_field='thumbnail_200x100', template="blog/thumbnail.html")
    list_display_links = ('admin_thumbnail', 'case_number')
    list_filter = ('case_manager', 'status', 'conclusion', 'date_occured',)
    ordering = ['date_occured']
    exclude = ('thumbnail_200x100', 'thumbnail_500x300', 'thumbnail_700x300', 'slug')

admin.site.register(Case, CaseAdmin)


class AudioEvidenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(AudioEvidence, AudioEvidenceAdmin)


class ImageEvidenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ImageEvidence, ImageEvidenceAdmin)


class PersonalExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(PersonalExperience, PersonalExperienceAdmin)


class VideoEvidenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(VideoEvidence, VideoEvidenceAdmin)


class MiscEvidenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(MiscEvidence, MiscEvidenceAdmin)


class GuestInvestigatorAdmin(admin.ModelAdmin):
    pass

admin.site.register(GuestInvestigator, GuestInvestigatorAdmin)
