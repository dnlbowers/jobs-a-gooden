from django.contrib import admin
from .models import Job, Notes, PinnedJobs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):
    """"
    Allows admin to manage jobs data via the admin panel
    """

    list_display = (
        'company_name',
        'job_title',
        'date_expired',
        'status',
        'approved'
        )
    list_filter = (
        'company_name',
        'job_title',
        'date_posted',
        'date_expired',
        'status',
        'approved',
        'is_pinned'
    )
    search_fields = (
        'company_name',
        'job_title',
    )
    summer_fields = (
        'job_description',
        )
    actions = [
        'approve_job',
        'hide_job',
        'make_public'
        ]

    def approve_job(self, request, queryset):
        """"
        Approve a user submitted job post
        """
        queryset.update(approved=True)

    def hide_job(self, request, queryset):
        """
        Change the status of a job to hidden
        """
        queryset.update(status=0)

    def make_public(self, request, queryset):
        """
        Change the status of a job to public
        """
        queryset.update(status=1)


@admin.register(PinnedJobs)
class PinnedJobsAdmin(admin.ModelAdmin):
    """
    Allows Admin to see which posts are pinned by a specific user
    """

    list_display = [
        'user',
        ]
    search_fields = [
        'user',
        ]
    list_filter = (
        'user',
        )


@admin.register(Notes)
class NoteAdmin(admin.ModelAdmin):
    """
    Allows admin to see how the feature is being used or not
    but hides the specific note content for dataprotection.
    """

    exclude = (
        'short_description',
        'note'
        )

    list_display = (
        'user',
        'related_job',
        'date_created',
        'is_insight'
    )

    list_filter = (
        'user',
        'related_job',
        'is_insight',
        'date_created'
    )

    search_fields = [
        'user__username',
        'related_job__company_name',
        'related_job__job_title',
        'date_created'
    ]
