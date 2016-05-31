from django.contrib import admin

from .models import Project
from imagekit.admin import AdminThumbnail

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'title', 'author', 'slug', 'publish', 'date_published')
    admin_thumbnail = AdminThumbnail(image_field='thumbnail_200x100', template="blog/thumbnail.html")
    list_display_links = ('admin_thumbnail', 'title',)
    list_filter = ('author', 'publish', 'date_published',)
    ordering = ['date_published']
    exclude = ('thumbnail_200x100', 'thumbnail_500x300', 'thumbnail_700x400', 'slug',)

admin.site.register(Project, ProjectAdmin)