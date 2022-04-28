from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('job_search.urls'), name='search_urls'),
    path('accounts/', include('allauth.urls')),
]

handler404 = 'job_search.views.error_404'
handler500 = 'job_search.views.error_500'
