from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.api.views.portfolio import (
    ProfileAPIView, TechCategoryViewSet, TechStackViewSet, ProjectViewSet,
    ExperienceViewSet, EducationViewSet, CertificationViewSet, ContactSubmissionViewSet
)

router = DefaultRouter()
router.register('tech-categories', TechCategoryViewSet, basename='tech-categories')
router.register('tech-stacks', TechStackViewSet, basename='tech-stacks')
router.register('projects', ProjectViewSet, basename='projects')
router.register('experiences', ExperienceViewSet, basename='experiences')
router.register('educations', EducationViewSet, basename='educations')
router.register('certifications', CertificationViewSet, basename='certifications')
router.register('contact-submissions', ContactSubmissionViewSet, basename='contact-submissions')

urlpatterns = [
    path('profile/', ProfileAPIView.as_view(), name='api-profile'),
    path('', include(router.urls)),
]
