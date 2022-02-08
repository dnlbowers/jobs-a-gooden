from django.urls import path
from . import views

urlpatterns = [
	path('jobsearch/', views.job_search, name='job_search'),
	path('listing/<str:pk>/', views.full_listing, name='full_listing'),
	path('pinboard', views.pinned_posts, name='pin_board'),
]