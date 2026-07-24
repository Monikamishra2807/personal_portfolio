from django import forms
from apps.education.models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'year', 'description']
        widgets = {
            'year': forms.TextInput(attrs={'type': 'text', 'placeholder': 'e.g., 2020 - 2024'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Brief description of your education'}),
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if not year:
            raise forms.ValidationError('Year is required')
        if len(year) < 4:
            raise forms.ValidationError('Please enter a valid year')
        return year
