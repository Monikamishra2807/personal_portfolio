from django import forms
from apps.projects.models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','short_description','description','github_url','live_url','video_demo','is_featured']
        widgets = {'description': forms.Textarea(attrs={'rows': 5})}
