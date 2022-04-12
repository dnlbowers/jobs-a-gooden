from django.urls import path
from . import views

urlpatterns = [
     # Temporarily set jobsearch to home page
     path('', views.JobList.as_view(
          extra_context={'title': 'Open Positions'}
          ), name='job_list'),
     # how do I add title to these views?
     path('fulldetails/<uuid:id>/',
          views.FullJobSpec.as_view(), name='job_details'),
     path('addjob/', views.AddJob.as_view(), name='add_job'),
     path('fulldetails/<uuid:id>/delete',
          views.DeleteJob.as_view(), name='delete_job'),
     path('fulldetails/<uuid:pk>/edit',
          views.EditJob.as_view(), name='edit_job'),
     # Pinning posts to save them
     path('pinboard/', views.PinnedPosts.as_view(), name='pin_board'),
     path('pinned/<uuid:id>/', views.PinJob.as_view(), name='pinned_job'),
     # Notes and insights to track progress
     path('addnote/<int:pk>/fulldetails/<uuid:id>/',
          views.FullJobSpec.as_view(), name='add_note'),
     path('insights/', views.DisplayInsights.as_view(), name='insights'),
     path('insights/add', views.AddInsight.as_view(), name='add_insight'),
     path('<id>/deletenote/', views.DeleteNote.as_view(), name='delete_note'),
     path('note/<int:pk>/edit/', views.EditNote.as_view(), name='edit_note'),
     path('insight/<int:pk>/edit/',
          views.EditInsight.as_view(), name='edit_insight'),
]
