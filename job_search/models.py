from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
STATUS = ((0, 'hidden'), (1, 'Public'))


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
    status = models.IntegerField(choices=STATUS, default=0)
    is_pinned = models.ManyToManyField(
        User, related_name='is_pinned', blank=True
    )

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'{self.company_name} -  {self.job_title}'


class PinnedJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pinned_jobs = models.ManyToManyField(
        Job, related_name='pinned_jobs', blank=True
        )

    def __str__(self):
        return f'{self.user.username}\'s pinned jobs'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        PinnedJobs.objects.create(user=instance)


class Notes(models.Model):

    related_job = models.ForeignKey(Job, on_delete=models.CASCADE, default=False, related_name='related_job')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    short_description = models.CharField(
        max_length=200, blank=False, null=False)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_insight = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.job.company_name + " - " + self.job.job_title + \
            "-" + "noted by " + self.user.username
