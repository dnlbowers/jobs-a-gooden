from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from .models import Job, PinnedJobs

# ~ADD DOCSTRINGS

class JobList(generic.ListView):
    model = Job
    paginate_by = 6
    template_name = 'job_search/pages/job-list.html'
    context_object_name = 'jobs'
    queryset = Job.objects.filter(status=1).order_by('-date_posted')


class FullJobSpec(View):
    def get(self, request, id, *args, **kwargs):
        queryset = Job.objects.filter(status=1)
        job_spec = get_object_or_404(queryset, id=id)
        pinned = False
        if job_spec.is_pinned.filter(id=self.request.user.id).exists():
            pinned = True

        return render(
            request,
            'job_search/pages/job-details.html',
            {
                "job": job_spec,
                "pinned": pinned,
            },
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Job.objects.filter(status=1)
        job_spec = get_object_or_404(queryset, id=id)
        pinned = False
        if job_spec.is_pinned.filter(id=self.request.user.id).exists():
            pinned = True

        return render(
            request,
            'job_search/pages/job-details.html',
            {
                "job": job_spec,
                "pinned": pinned,
            },
        )


class PinJob(View):
    def post(self, request, id):
        # get the status of the toggle from post request in JS file
        status = True if request.POST['status'] == 'true' else False
        # Identify the job being toggled
        job = Job.objects.get(id=id)
        # identify the users pinned job database table
        pinned = PinnedJobs.objects.get(user=request.user)

        if status:
            # add to manytomany list
            pinned.pinned_jobs.add(job)
            # add user to is_pinned
            job.is_pinned.add(request.user)
        else:
            # remove from manytomany list
            pinned.pinned_jobs.remove(job)
            # remove user from is_pinned
            job.is_pinned.remove(request.user)

        return HttpResponse(200)


# class PinnedJobBoard(generic.ListView):
#     model = PinnedJobs
#     paginate_by = 6
#     template_name = 'job_search/pages/pinboard.html'
#     context_object_name = 'jobs'
    
#     def get_queryset(self):
#         return super().get_queryset()
    
    
# How to paginate? 
def pinned_posts(request):
    # get all pinned posts by user
    pinned = PinnedJobs.objects.get(user=request.user)
    # get all jobs from the many to many list
    jobs = pinned.pinned_jobs.all()
    return render(request, 'job_search/pages/pinboard.html', {'jobs': jobs})
