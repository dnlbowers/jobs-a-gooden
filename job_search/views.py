from django.shortcuts import render



def job_search(request):
    return render(request, 'job_search/pages/job-search.html')


def full_listing(request, pk):
    jobid = pk
    return render(request, 'job_search/pages/full-listing.html', {'job': jobid})


def pinned_posts(request):
    return render(request, 'pages/pinboard.html')
