from django.db import models
import uuid

# Create your models here.
class JobSearch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=400)
    location = models.CharField(max_length=200)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    job_description = models.TextField()
    job_url = models.URLField(max_length=200)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name + " - " + self.job_title
