from django import forms
from apps.certifications.models import Certification


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuer', 'issue_date', 'credential_url', 'preview_image']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'credential_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
