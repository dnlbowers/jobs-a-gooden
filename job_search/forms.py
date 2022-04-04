from .models import Notes, Job
from django import forms
from django_summernote.widgets import SummernoteWidget


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('short_description', 'note', 'is_insight', )
        widgets = {
            'note': SummernoteWidget(),
        }


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'company_name',
            'job_title', 'location',
            'min_salary',
            'max_salary',
            'currency',
            'date_expired',
            'job_description',
            'job_url',
            'status'
            ]
        widgets = {
            'job_description': SummernoteWidget(),
        }
