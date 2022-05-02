"""
This file contains the form structure
for license purchases
"""

from django import forms
from .models import LicensePurchase


class LicensePurchaseForm(forms.ModelForm):
    """
    The form that the user must fill in
    order to complete a license purchase
    """

    class Meta:
        """
        Associate form with License Purchase
        model & exclude user, stripe & date
        related fields
        """

        model = LicensePurchase
        fields = [
            "purchaser_full_name",
            "purchaser_email",
            "purchaser_phone_number",
            "purchaser_street_address1",
            "purchaser_street_address2",
            "purchaser_town_or_city",
            "purchaser_postcode",
            "purchaser_county",
            "purchaser_country",
            "no_of_licenses_purchased",
        ]

    def __init__(self,  *args, **kwargs):
        """
        Insert placeholders
        on intialization
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "purchaser_full_name": "e.g. Kathleen Booth",
            "purchaser_email": "e.g. kathleenbooth@email.com",
            "purchaser_phone_number": "e.g. 07123456789",
            "purchaser_street_address1": "e.g. 44",
            "purchaser_street_address2": "e.g. Chester Road",
            "purchaser_town_or_city": "e.g. Crawley",
            "purchaser_postcode": "e.g. RH10 1EJ",
            "purchaser_county": "e.g. Sussex",
            "purchaser_country": "Select Country",
            "no_of_licenses_purchased": "Amount of Licenses"
        }
        labels = {
            "purchaser_full_name": "Full Name",
            "purchaser_email": "Email Address",
            "purchaser_phone_number": "Phone Number",
            "purchaser_street_address1": "Street Address 1",
            "purchaser_street_address2": "Street Address 2",
            "purchaser_town_or_city": "Town / City",
            "purchaser_postcode": "Post Code",
            "purchaser_county": "County",
            "purchaser_country": "Country",
            "no_of_licenses_purchased": "Amount of Licenses"
        }

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            self.fields[field].widget.attrs['placeholder'] = placeholders[
                field
            ]
            self.fields[field].label = labels[field]
