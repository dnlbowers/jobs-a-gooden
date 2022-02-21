from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid


# Create your models here.
class Job(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=400)
    location = models.CharField(max_length=200)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    job_description = models.TextField()
    job_url = models.URLField(max_length=2000)
    is_pinned = models.BooleanField(
        'PinnedJob', default=False
        )

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.company_name + " - " + self.job_title

    def job_is_pinned(self):
        return self.is_pinned


class PinnedJob(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)  # Wanted this to have a condition if not pinned then delete
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_pinned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.company_name + " - " + self.job.job_title + \
            "-" + "pinned by"  # + self.user.username


class Notes(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)
    pinned_job = models.ForeignKey(PinnedJob, on_delete=models.CASCADE)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    short_description = models.CharField(
        max_length=200, default=False, blank=True, null=True)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_insight = models.BooleanField(default=False)

    def __str__(self):
        return self.job.company_name + " - " + self.job.job_title + \
            "-" + "noted by "  # + self.user.username
