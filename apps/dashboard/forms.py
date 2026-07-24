from django import forms
from apps.projects.models import Project
from apps.portfolio.models import Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','short_description','description','github_url','live_url','video_demo','is_featured']
        widgets = {'description': forms.Textarea(attrs={'rows': 5})}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'role', 'tagline', 'biography', 'experience_summary', 'skills_summary', 'location', 'is_available', 'email', 'phone', 'address']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4}),
            'experience_summary': forms.Textarea(attrs={'rows': 4}),
            'skills_summary': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }
