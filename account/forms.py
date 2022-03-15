"""
This file contains the form structure for accounts
"""

from django import forms
from .models import UserAccount


class AccountDetailsForm(forms.ModelForm):
    """
    The form which covers the user's general info
    """

    class Meta:
        """
        Associate form with UserAccount model &
        exclude billing oriented details
        """
        model = UserAccount
        exclude = (
            'user',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_postcode',
            'default_county',
            'default_country'
        )

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
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'default_phone_number': 'Phone Number'
        }

        # Auto focus on the first field
        self.fields['first_name'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:
            # Add * for each required field
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Give them their respective placeholders & classes
            self.fields[field].widget.attrs['placeholder'] = placeholder


class BillingDetailsForm(forms.ModelForm):
    """
    The form which covers the user's
    default billing information
    """

    class Meta:
        """
        Associate form with UserAccount model &
        exclude personal info details
        """
        model = UserAccount
        exclude = (
            'user',
            'first_name',
            'last_name',
            'default_phone_number'
        )

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
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Auto focus on the first field
        self.fields['default_street_address1'].widget.attrs['autofocus'] = True

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
