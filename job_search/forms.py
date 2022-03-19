from .models import Notes
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('short_description', 'note', 'is_insight', )
