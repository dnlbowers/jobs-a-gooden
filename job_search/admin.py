from django.contrib import admin
from .models import Job, PinnedJob, Notes
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    list_display = (
        'company_name', 'job_title', 'date_expired', 'status'
        )
    list_filter = (
        'company_name', 'job_title', 'date_posted', 'date_expired', 'is_pinned'
    )
    search_fields = (
        'company_name', 'job_title', 'date_posted', 'date_expired', 'is_pinned'
    )
    summer_fields = ('job_description',)


admin.site.register(PinnedJob)


admin.site.register(Notes)
