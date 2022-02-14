from django.contrib import admin

# Register your models here.
from .models import Job, PinnedJob, Notes 

admin.site.register(Job)
admin.site.register(PinnedJob)
admin.site.register(Notes)
