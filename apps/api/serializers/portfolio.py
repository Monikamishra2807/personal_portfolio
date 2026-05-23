from rest_framework import serializers
from apps.portfolio.models import Profile, TechStack, TechCategory, SocialLink
from apps.projects.models import Project, ProjectTag
from apps.experience.models import Experience
from apps.education.models import Education
from apps.certifications.models import Certification
from apps.contact.models import ContactSubmission
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta: model = SocialLink; fields = '__all__'
class TechStackSerializer(serializers.ModelSerializer):
    class Meta: model = TechStack; fields = '__all__'
class TechCategorySerializer(serializers.ModelSerializer):
    skills = TechStackSerializer(many=True, read_only=True)
    class Meta: model = TechCategory; fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    class Meta: model = Profile; fields = '__all__'
class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta: model = ProjectTag; fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = TechStackSerializer(many=True, read_only=True)
    tags = ProjectTagSerializer(many=True, read_only=True)
    class Meta: model = Project; fields = '__all__'
class ExperienceSerializer(serializers.ModelSerializer):
    tech_used = TechStackSerializer(many=True, read_only=True)
    class Meta: model = Experience; fields = '__all__'
class EducationSerializer(serializers.ModelSerializer):
    class Meta: model = Education; fields = '__all__'
class CertificationSerializer(serializers.ModelSerializer):
    class Meta: model = Certification; fields = '__all__'
class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta: model = ContactSubmission; fields = '__all__'
