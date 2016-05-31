from django.contrib import admin
from .models import Category, Tag, Post
from imagekit.admin import AdminThumbnail

def make_published(self, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "1 post was"
    else:
        message_bit = "%s posts were" % rows_updated
    self.message_user(request, "%s successfully marked as published." % message_bit)
make_published.short_description = "Mark selected posts as published"

def make_draft(self, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "1 post was"
    else:
        message_bit = "%s posts were" % rows_updated
    self.message_user(request, "%s successfully marked as draft." % message_bit)
make_draft.short_description = "Mark selected posts as draft"

def make_withdrawn(self, request, queryset):
    rows_updated = queryset.update(status='w')
    if rows_updated == 1:
        message_bit = "1 post was"
    else:
        message_bit = "%s posts were" % rows_updated
    self.message_user(request, "%s successfully marked as withdrawn." % message_bit)
make_withdrawn.short_description = "Mark selected posts as withdrawn"

class PostAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'title', 'author', 'slug', 'date_created', 'date_modified', 'status')
    admin_thumbnail = AdminThumbnail(image_field='thumbnail_200x100', template="blog/thumbnail.html")
    list_display_links = ('admin_thumbnail', 'title')
    list_filter = ('author', 'date_created', 'status')
    ordering = ['date_modified']
    actions = [make_published, make_draft, make_withdrawn]
    exclude = ('thumbnail_200x100', 'thumbnail_900x300', 'slug')

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)