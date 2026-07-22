from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from apps.contact.models import ContactSubmission


class ContactListView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/contact_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactSubmission.objects.all().order_by('-created_at')
        return context


class ContactResolveView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        contact = get_object_or_404(ContactSubmission, pk=pk)
        contact.is_resolved = True
        contact.save()
        return JsonResponse({'success': True, 'message': 'Contact marked as resolved'})

    def get(self, request, pk, *args, **kwargs):
        contact = get_object_or_404(ContactSubmission, pk=pk)
        contact.is_resolved = True
        contact.save()
        return JsonResponse({'success': True})
