"""
This file contains the form structure for the
Account Details & Billing Details form
found within the accounts app
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
        only include billing oriented details
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

    def __init__(self, *args, **kwargs):
        """
        Initialise with placeholders, labels &
        autofocus
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'profile_picture': 'Profile Picture (Use square ratios)',
            'first_name': 'e.g. Kathleen',
            'last_name': 'e.g. Booth',
            'phone_number': 'e.g. 07123456789',
            'github_profile': 'https://github.com/...',
            'linkedin_profile': 'https://www.linkedin.com/in/...'
        }
        labels = {
            'profile_picture': 'Profile Picture (Use square ratios)',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'github_profile': 'GitHub Profile URL',
            'linkedin_profile': 'LinkedIn Profile URL'
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].label = labels[field]
            if field != 'profile_picture':
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholders[field]


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
        Initialise with placeholders, labels &
        autofocus
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

        self.fields['default_street_address1'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].label = labels[field]

            if field != 'default_country':
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholders[field]
