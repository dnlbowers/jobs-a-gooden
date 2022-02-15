from django.contrib import admin

# Register your models here.
from .models import Job, PinnedJob, Notes 


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'job_title', 'date_expired', 'is_pinned'
        )
    list_filter = (
        'company_name', 'job_title', 'date_posted', 'date_expired', 'is_pinned'
    )
    search_fields = (
        'company_name', 'job_title', 'date_posted', 'date_expired', 'is_pinned'
    )

admin.site.register(PinnedJob)
admin.site.register(Notes)
