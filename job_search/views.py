from django.shortcuts import render
from django.http import HttpResponse

def job_search(request):
    return HttpResponse('Here are the returned job posts')

def full_listing(request, pk):
    return HttpResponse(f'Here is the full job specs for job id {pk}')

def pinned_posts(request):
    return HttpResponse('Here will be your saved pinned posts')

