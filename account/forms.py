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
        fields = [
            'profile_picture',
            'first_name',
            'last_name',
            'phone_number',
            'github_profile',
            'linkedin_profile'
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
            'profile_picture': 'Profile Picture (Use square ratios)',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'github_profile': 'GitHub Profile URL',
            'linkedin_profile': 'LinkedIn Profile URL'
        }

        # Auto focus on the first field
        self.fields['first_name'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders & labels along the way
        for field in self.fields:
            # Add * for each required field
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Give them their respective placeholders & classes
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = placeholder


class BillingDetailsForm(forms.ModelForm):
    """
    The form which covers the user's
    default billing information
    """

    class Meta:
        """
        Associate form with UserAccount model &
        only include billing info details
        """
        model = UserAccount
        fields = [
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_postcode',
            'default_county',
            'default_country'
        ]

    def __init__(self, *args, **kwargs):
        """
        Here we insert placeholders & 
        set autofocus to the first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_street_address1': 'e.g. 44',
            'default_street_address2': 'e.g. Chester Road',
            'default_town_or_city': 'e.g. Crawley',
            'default_postcode': 'e.g. RH10 1EJ',
            'default_county': 'e.g. Sussex',
            'default_country': 'Select Country'
        }
        labels = {
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town / City',
            'default_postcode': 'Post Code',
            'default_county': 'County',
            'default_country': 'Select Country'
        }

        # Auto focus on the first field
        self.fields['default_street_address1'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:
            # Add * for each required field
            if self.fields[field].required:
                label = f'{labels[field]} *'
            else:
                label = labels[field]

            # Give them their respective placeholders & classes
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].label = label
