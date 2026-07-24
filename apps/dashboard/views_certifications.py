from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.certifications.models import Certification
from .forms_certifications import CertificationForm

class CertificationListView(LoginRequiredMixin, ListView):
    model = Certification
    template_name = 'dashboard/certification_list.html'
    context_object_name = 'certification_list'
    ordering = ['order']

class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'dashboard/certification_form.html'
    success_url = reverse_lazy('dashboard:certification_list')

class CertificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'dashboard/certification_form.html'
    success_url = reverse_lazy('dashboard:certification_list')

class CertificationDeleteView(LoginRequiredMixin, DeleteView):
    model = Certification
    success_url = reverse_lazy('dashboard:certification_list')
    template_name = 'dashboard/confirm_delete.html'

class CertificationDetailView(LoginRequiredMixin, DetailView):
    model = Certification
    template_name = 'dashboard/certification_detail.html'