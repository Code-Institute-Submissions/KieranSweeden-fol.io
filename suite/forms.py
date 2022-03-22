"""
This file contains various forms that relate
to the folio model
"""

from django import forms
from .models import Folio


class FolioContactForm(forms.ModelForm):
    """
    This form relates to the contact information
    within the folio model.
    """

    class Meta:

        # Meta options inform django what model
        # this class will be associated with
        model = Folio

        # Explicity telling django to only
        # load the fields relating to the folio's
        # contact information
        fields = [
            'contact_email',
            'contact_number',
            'contact_github_profile',
            'contact_linkedin_profile'
        ]
    
    # Customize the form
    def __init__(self, *args, **kwargs):
        """
        Here we insert placeholders & 
        set autofocus to the first field
        """

        # Set the form up as it would be by default
        super().__init__(*args, **kwargs)

        # Prepare placeholders
        placeholders = {
            'contact_email': 'Email address',
            'contact_number': 'Phone number',
            'contact_github_profile': 'GitHub profile URL',
            'contact_linkedin_profile': 'LinkedIn profile URL'
        }

        # Auto focus on the first field
        self.fields['contact_email'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
