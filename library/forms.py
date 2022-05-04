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
        # Form is associated with the Folio model
        model = Folio

        # Explicity telling django to only load
        # the name & description fields
        fields = [
            'name',
            'description'
        ]

        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3
            })
        }

    # Customize the form
    def __init__(self, *args, **kwargs):
        """
        Here we insert placeholders &
        set autofocus to the first field in form
        """

        # Set the form up as it would be by default
        super().__init__(*args, **kwargs)

        # Prepare placeholders
        placeholders = {
            'name': 'e.g. "Front-End Folio" or "MERN Stack Folio"',
            'description': 'e.g. A folio showcasing my front-end abilities'
        }
        labels = {
            'name': 'Folio Name',
            'description': 'Folio Description'
        }

        # Auto focus on the first field
        self.fields['name'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders & labels along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            self.fields[field].widget.attrs['placeholder'] = placeholders[
                field
            ]
            self.fields[field].label = labels[field]
