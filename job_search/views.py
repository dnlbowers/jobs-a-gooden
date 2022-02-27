from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

        return render(
            request, 'job_search/pages/job-details.html',
            {"job": job_spec}
            )


def pinned_posts(request):
    return render(request, 'pages/pinboard.html')
