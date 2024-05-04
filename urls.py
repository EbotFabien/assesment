from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('risk_assessment_project.urls')),  # Include risk_assessment_project URLs
]
