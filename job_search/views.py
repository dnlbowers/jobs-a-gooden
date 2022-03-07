from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Job


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
    def pin_job(self, request, id):
        pinned_job = get_object_or_404(Job, id=id)

        if pinned_job.is_pinned.filter(id=request.user.id).exist():
            pinned_job.is_pinned.remove(request.user)
        else:
            pinned_job.is_pinned.add(request.user)

        return HttpResponseRedirect(reverse('full_job_details', args=[id]))


def pinned_posts(request):
    return render(request, 'pages/pinboard.html')
