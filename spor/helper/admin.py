from django.contrib import admin
from .models import FAQ, KnownIssue, BugCategory, BugReport

class FAQAdmin(admin.ModelAdmin):
    pass

admin.site.register(FAQ, FAQAdmin)

class KnownIssueAdmin(admin.ModelAdmin):
    pass

admin.site.register(KnownIssue, KnownIssueAdmin)

class BugCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BugCategory, BugCategoryAdmin)

class BugReportAdmin(admin.ModelAdmin):
    list_display = ('category', 'date_submitted', 'severity', 'status', 'assignee')
    list_filter = ('category', 'severity', 'status', 'assignee')
    ordering = ['date_submitted']

admin.site.register(BugReport, BugReportAdmin)