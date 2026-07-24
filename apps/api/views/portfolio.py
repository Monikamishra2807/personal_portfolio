from django.http import Http404
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.portfolio.models import Profile, TechCategory, TechStack
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education
from apps.certifications.models import Certification
from apps.contact.models import ContactSubmission
from apps.api.serializers.portfolio import (
    ProfileSerializer, TechCategorySerializer, TechStackSerializer,
    ProjectSerializer, ExperienceSerializer, EducationSerializer,
    CertificationSerializer, ContactSubmissionSerializer
)

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users (staff) to edit objects,
    but allow read-only access to anyone.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete the singular personal Profile.
    Supports POST if no Profile exists yet.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_object(self):
        obj = Profile.objects.first()
        if not obj:
            raise Http404("No profile exists yet.")
        return obj

    def post(self, request, *args, **kwargs):
        if Profile.objects.exists():
            return Response(
                {"detail": "Profile already exists. Use PUT or PATCH to update it."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TechCategoryViewSet(viewsets.ModelViewSet):
    queryset = TechCategory.objects.all()
    serializer_class = TechCategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class TechStackViewSet(viewsets.ModelViewSet):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().prefetch_related('tech_stack', 'tags')
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filterset_fields = ['is_featured']

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint to list, retrieve, update or delete contact submissions (Admin only).
    Allows public POST (create) to submit a contact request.
    """
    queryset = ContactSubmission.objects.all().order_by('-created_at')
    serializer_class = ContactSubmissionSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [IsAdminUser()]
