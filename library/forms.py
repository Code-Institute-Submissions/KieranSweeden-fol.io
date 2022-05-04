"""
This file contains the forms used to
create & update folios
"""

from django import forms
from suite.models import Folio


class CreateFolioForm(forms.ModelForm):
    """
    This form creates a new folio for the user
    """
    class Meta:
        model = Folio
        fields = [
            'name',
            'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3
            })
        }

    def __init__(self, *args, **kwargs):
        """
        Here we insert placeholders &
        set autofocus to the first field in form
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'e.g. "Front-End Folio" or "MERN Stack Folio"',
            'description': 'e.g. A folio showcasing my front-end abilities'
        }
        labels = {
            'name': 'Folio Name',
            'description': 'Folio Description'
        }

        for field in self.fields:
            self.fields[field].widget.attrs[
                'placeholder'] = placeholders[field]
            self.fields[field].label = labels[field]
