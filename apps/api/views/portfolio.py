from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from apps.portfolio.models import Profile, TechCategory
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education
from apps.certifications.models import Certification
from apps.contact.models import ContactSubmission
from apps.api.serializers.portfolio import ProfileSerializer, TechCategorySerializer, ProjectSerializer, ExperienceSerializer, EducationSerializer, CertificationSerializer, ContactSubmissionSerializer
class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    def get_object(self): return Profile.objects.first()
class TechStackAPIView(generics.ListAPIView):
    queryset = TechCategory.objects.filter(is_active=True).prefetch_related('skills')
    serializer_class = TechCategorySerializer
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_active=True).prefetch_related('tech_stack', 'tags')
    serializer_class = ProjectSerializer
    filterset_fields = ['is_featured']
class ExperienceAPIView(generics.ListAPIView):
    queryset = Experience.objects.filter(is_active=True)
    serializer_class = ExperienceSerializer
class EducationAPIView(generics.ListAPIView):
    queryset = Education.objects.filter(is_active=True)
    serializer_class = EducationSerializer
class CertificationAPIView(generics.ListAPIView):
    queryset = Certification.objects.filter(is_active=True)
    serializer_class = CertificationSerializer
class ContactSubmissionAPIView(generics.ListAPIView):
    queryset = ContactSubmission.objects.all().order_by('-created_at')
    serializer_class = ContactSubmissionSerializer
    permission_classes = [IsAdminUser]
