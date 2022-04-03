from django.urls import path
from . import views

urlpatterns = [
    # Temporarily set jobsearch to home page
    path('', views.JobList.as_view(
        extra_context={'title': 'Open Positions'}
        ), name='job_list'),
    # how do I add title to these views?
    path('fulldetails/<uuid:id>/', views.FullJobSpec.as_view(), name='job_details'),
    path('addjob/', views.AddJob.as_view(), name='add_job'),
    path('fulldetails/<uuid:id>/delete', views.DeleteJob.as_view(), name='delete_job'),
    # Pinning posts to save them
    path('pinboard/', views.PinnedPosts.as_view(), name='pin_board'),
    path('pinned/<uuid:id>/', views.PinJob.as_view(), name='pinned_job'),
    # Notes and insights to track progress
    path('fulldetails/<uuid:id>/note/', views.FullJobSpec.as_view(), name='note_made'),
    path('insights/', views.DisplayInsights.as_view(), name='insights'),
    path('<id>/deletenote/', views.DeleteNote.as_view(), name='delete_note'),
]
