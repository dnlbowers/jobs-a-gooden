from django.shortcuts import render
from django.http import HttpResponse


def job_search(request):
    return render(request, 'job_search/pages/job-search.html')


def full_listing(request, pk):
    return render(request, 'job_search/pages/full-listing.html')


def pinned_posts(request):
    return render(request, 'pages/pinboard.html')
