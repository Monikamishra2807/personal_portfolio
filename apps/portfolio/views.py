from django.views.generic import TemplateView
from .models import Profile, TechCategory
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education
from apps.certifications.models import Certification
class HomeView(TemplateView):
    template_name = 'portfolio/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['tech_categories'] = TechCategory.objects.filter(is_active=True).prefetch_related('skills')
        context['featured_projects'] = Project.objects.filter(is_active=True, is_featured=True).prefetch_related('tech_stack', 'tags', 'gallery')[:6]
        context['experiences'] = Experience.objects.filter(is_active=True).prefetch_related('tech_used')
        context['education_list'] = Education.objects.filter(is_active=True)
        context['certifications'] = Certification.objects.filter(is_active=True)
        return context
class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
