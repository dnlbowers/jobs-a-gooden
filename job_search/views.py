from django.shortcuts import render
from django.views import generic
from .models import Job


class JobList(generic.ListView):
    model = Job
    paginate_by = 6
    template_name = 'job_search/pages/job-list.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']

def job_search(request):
    return render(request, 'job_search/pages/job-search.html')


def full_listing(request, pk):
    jobid = pk
    return render(
        request, 'job_search/pages/full-listing.html', {'job': jobid}
        )


def pinned_posts(request):
    return render(request, 'pages/pinboard.html')
