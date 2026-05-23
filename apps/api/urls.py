from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.api.views.portfolio import ProfileAPIView, TechStackAPIView, ProjectViewSet, ExperienceAPIView, EducationAPIView, CertificationAPIView, ContactSubmissionAPIView
router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
urlpatterns = [
    path('profile/', ProfileAPIView.as_view(), name='api-profile'),
    path('tech-stack/', TechStackAPIView.as_view(), name='api-tech-stack'),
    path('experience/', ExperienceAPIView.as_view(), name='api-experience'),
    path('education/', EducationAPIView.as_view(), name='api-education'),
    path('certifications/', CertificationAPIView.as_view(), name='api-certifications'),
    path('contact-submissions/', ContactSubmissionAPIView.as_view(), name='api-contact-submissions'),
    path('', include(router.urls)),
]
