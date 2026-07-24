from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.portfolio.models import SocialLink
from .forms_social_links import SocialLinkForm

class SocialLinkListView(LoginRequiredMixin, ListView):
    model = SocialLink
    template_name = 'dashboard/social_links_list.html'
    context_object_name = 'social_links'
    ordering = ['order']

class SocialLinkCreateView(LoginRequiredMixin, CreateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = 'dashboard/social_link_form.html'
    success_url = reverse_lazy('dashboard:social_links_list')

class SocialLinkUpdateView(LoginRequiredMixin, UpdateView):
    model = SocialLink
    form_class = SocialLinkForm
    template_name = 'dashboard/social_link_form.html'
    success_url = reverse_lazy('dashboard:social_links_list')

class SocialLinkDeleteView(LoginRequiredMixin, DeleteView):
    model = SocialLink
    success_url = reverse_lazy('dashboard:social_links_list')
    template_name = 'dashboard/confirm_delete.html'

class SocialLinkDetailView(LoginRequiredMixin, DetailView):
    model = SocialLink
    template_name = 'dashboard/social_link_detail.html'