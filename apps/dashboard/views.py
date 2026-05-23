from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from apps.projects.models import Project
from .forms import ProjectForm
class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:10]
        context['project_form'] = ProjectForm()
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
