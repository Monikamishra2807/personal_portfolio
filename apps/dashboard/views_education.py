from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.education.models import Education
from .forms_education import EducationForm

class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'dashboard/education_list.html'
    context_object_name = 'education_list'
    ordering = ['order']

class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'dashboard/education_form.html'
    success_url = reverse_lazy('dashboard:education_list')

class EducationUpdateView(LoginRequiredMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'dashboard/education_form.html'
    success_url = reverse_lazy('dashboard:education_list')

class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    success_url = reverse_lazy('dashboard:education_list')
    template_name = 'dashboard/confirm_delete.html'

class EducationDetailView(LoginRequiredMixin, DetailView):
    model = Education
    template_name = 'dashboard/education_detail.html'