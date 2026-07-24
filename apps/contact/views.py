from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from .forms import ContactForm
class ContactSubmitView(View):
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            send_mail(obj.subject, obj.message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
            return render(request, 'partials/contact_success.html', {'message': 'Thanks! Your message has been sent.'})
        return render(request, 'partials/contact_form.html', {'form': form}, status=400)
