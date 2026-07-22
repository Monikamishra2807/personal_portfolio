from django import forms
from apps.portfolio.models import SocialLink


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url', 'icon', 'is_active']
        widgets = {
            'platform': forms.TextInput(attrs={'placeholder': 'e.g., GitHub, LinkedIn, Twitter'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://example.com/your-profile'}),
            'icon': forms.TextInput(attrs={'placeholder': 'e.g., github, linkedin, twitter'}),
        }

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if url and not url.startswith(('http://', 'https://')):
            raise forms.ValidationError('URL must start with http:// or https://')
        return url
