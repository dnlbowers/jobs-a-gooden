from django.urls import path
from . import views

urlpatterns = [
    # Temporarily set jobsearch to home page
    path('', views.job_search, name='job_search'),
    path('listing/<str:pk>/', views.full_listing, name='full_listing'),
    path('pinboard', views.pinned_posts, name='pin_board'),
]
