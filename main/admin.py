from django.contrib import admin

# Register your models here.
from .models import *


admin.site.site_header = "CDOE - DAVV Admin Panel"
admin.site.site_title = "CDOE - DAVV Admin Panel"

admin.site.register(Program)
admin.site.register(CourseDetail)
admin.site.register(CourseType)
admin.site.register(Announcement)
admin.site.register(Notice)
admin.site.register(Faculty)
admin.site.register(Index)
admin.site.register(ComingSoonMailList)
admin.site.register(Slide)
admin.site.register(UsefulLink)
admin.site.register(Team)
# admin.site.register(Review)

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Mail to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterAdmin)