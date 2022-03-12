from django.urls import path
from . import views

urlpatterns = [
    # Temporarily set jobsearch to home page
    path('', views.JobList.as_view(
        extra_context={'title': 'Open Positions'}
        ), name='job_list'),
    # how do I add title to these views?
    path('<uuid:id>/', views.FullJobSpec.as_view(), name='job_details'),
    path('pinboard', views.pinned_posts, name='pin_board'),
    path('pinned/<uuid:id>/', views.PinJob.as_view(), name='pinned_job')
]
