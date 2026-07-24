from django.views.generic import TemplateView
from django.views.generic import RedirectView
from .models import Profile, TechCategory, SocialLink
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education
from apps.certifications.models import Certification
from apps.portfolio.models import SocialLink as PortfolioSocialLink


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['social_links'] = SocialLink.objects.filter(is_active=True).order_by('order')
        context['tech_categories'] = TechCategory.objects.filter(is_active=True).prefetch_related('skills')
        context['featured_projects'] = Project.objects.filter(is_active=True, is_featured=True).prefetch_related('tech_stack', 'tags')[:6]
        context['experiences'] = Experience.objects.filter(is_active=True).prefetch_related('tech_used')
        context['education_list'] = Education.objects.filter(is_active=True)[:3]
        context['certifications'] = Certification.objects.filter(is_active=True)[:4]
        return context


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class Custom404View(TemplateView):
    template_name = 'portfolio/404.html'
    status_code = 404


class Custom403View(TemplateView):
    template_name = 'portfolio/403.html'
    status_code = 403


class Custom500View(TemplateView):
    template_name = 'portfolio/500.html'
    status_code = 500
