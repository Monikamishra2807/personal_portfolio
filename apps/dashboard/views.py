from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from apps.projects.models import Project
from apps.portfolio.models import Profile
from .forms import ProjectForm, ProfileForm

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:10]
        context['project_form'] = ProjectForm()
        context['profile_form'] = ProfileForm(instance=Profile.objects.first())
        return context

class DashboardProjectListView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/project_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

class DashboardProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('dashboard:home')
    def form_valid(self, form):
        self.object = form.save()
        if self.request.htmx:
            return render(self.request, 'dashboard/partials/project_row.html', {'project': self.object})
        return super().form_valid(form)
    def form_invalid(self, form):
        return render(self.request, 'dashboard/partials/project_form.html', {'project_form': form}, status=400)

class DashboardProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'dashboard/project_form.html'
    success_url = reverse_lazy('dashboard:project_list')

class DashboardProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/confirm_delete.html'

class DashboardProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'dashboard/project_detail.html'

class DashboardProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'dashboard/profile_form.html'
    success_url = reverse_lazy('dashboard:home')

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(
            defaults={
                'name': 'Your Name',
                'role': 'Your Role',
                'tagline': 'Your Tagline',
            }
        )
        return profile
