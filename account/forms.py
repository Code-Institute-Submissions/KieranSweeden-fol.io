"""
This file contains the form structure for accounts
"""

from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    """
    The form which covers the user's general info
    & default billing information
    """

    class Meta:
        """
        Associate form with UserAccount model
        """
        model = UserAccount
        exclude = ('user',)

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
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Auto focus on the first field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:
            if field != "default_country":
                # Add * for each required field
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # Give them their respective placeholders & classes
                self.fields[field].widget.attrs['placeholder'] = placeholder
