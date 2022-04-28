from .models import Notes, Job
from django import forms
from django_summernote.widgets import SummernoteWidget


class DateInput(forms.DateInput):
    """ Date input for job expiry date field"""
    input_type = 'date'


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('short_description', 'note', 'is_insight', )
        widgets = {
            'note': SummernoteWidget(),
        }


class AddJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddJobForm, self).__init__(*args, **kwargs)
        self.fields['job_url'].widget.attrs = (
            {'placeholder': 'Must begin http:// or https://'}
        )
        self.fields['currency'].widget.attrs = (
            {'placeholder': 'USD, EUR, GBP, etc'}
        )
        self.fields['min_salary'].widget.attrs = (
            {'placeholder': 'numbers only, no ", " or "."'}
        )
        self.fields['max_salary'].widget.attrs = (
            {'placeholder': 'numbers only, no ", " or "."'}
        )

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
        ]

        widgets = {
            'job_description': SummernoteWidget(),
            'date_expired': DateInput(attrs={'class': 'form-field'}),
        }
