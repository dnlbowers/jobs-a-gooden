from django.urls import path
from . import views

urlpatterns = [
     # READ

     # Page to display all job opening in a list view (6 per page)
     path('', views.JobList.as_view(
          extra_context={'title': 'Open Positions'}
          ), name='job_list'),

     # Page to display all insights in a list view (6 per page)
     path('insights/', views.DisplayInsights.as_view(
          extra_context={'title': 'Insights'}
          ), name='insights'),

     # Page to display the full job details and notes section when pinned
     path('fulldetails/<uuid:id>/',
          views.FullJobSpec.as_view(), name='job_details'),

     # Page to give the user instruction on how to use the tracking feature
     path(
          'trackinginstructions/', views.TrackingInstructions.as_view(),\
          name='tracking_instructions'
          ),

     # Page with contact details for the admin
     path('contact/', views.Contact.as_view(), name='contact'),

     # CREATE

     # Add job
     path('addjob/', views.AddJob.as_view(), name='add_job'),

     # Add job specific to the user and the job
     path('addnote/<int:pk>/fulldetails/<uuid:id>/',
          views.FullJobSpec.as_view(), name='add_note'),

     # add insight with no related job
     path('insights/add', views.AddInsight.as_view(), name='add_insight'),

     # DELETE

     # Delete job (admin only)
     path('fulldetails/<uuid:id>/delete',
          views.DeleteJob.as_view(), name='delete_job'),

     # Delete note
     path('<id>/deletenote/', views.DeleteNote.as_view(), name='delete_note'),

     # UPDATE

     # Edit Job (admin only)
     path('fulldetails/<uuid:pk>/edit',
          views.EditJob.as_view(), name='edit_job'),

     # Page to view saved jobs
     path('pinboard/', views.PinnedPosts.as_view(
          extra_context={'title': 'Saved Jobs'}
          ), name='pin_board'),

     # Pinning posts to save them
     path('pinned/<uuid:id>/', views.PinJob.as_view(), name='pinned_job'),

     # Edit note/insight related to specific job
     path('note/<int:pk>/edit/', views.EditNote.as_view(), name='edit_note'),

     # Edit insight unrelated to a job
     path('insight/<int:pk>/edit/',
          views.EditInsight.as_view(), name='edit_insight'),
]
