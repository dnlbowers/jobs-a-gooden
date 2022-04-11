from django.contrib import admin
from .models import Job, Notes, PinnedJobs
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = (
        'company_name', 'job_title', 'date_expired', 'status', 'approved'
        )
    list_filter = (
        'company_name', 'job_title', 'date_posted', 'date_expired', 'status', 'approved'
    )
    search_fields = (
        'company_name', 'job_title', 'date_posted', 'date_expired', 'status', 'approved'
    )
    summer_fields = ('job_description',)
    actions = ['approve_job']

    def approve_job(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(PinnedJobs)


admin.site.register(Notes)
