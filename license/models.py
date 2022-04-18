"""
Models related to the license store
"""

from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

import uuid


class LicensePurchase(models.Model):
    """
    A license purchase which gets created
    when a user makes license purchase
    via the license store & stripe
    """

    # UserAccount the license purchase belongs to
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # General purchaser information
    purchaser_full_name = models.CharField(max_length=40)
    purchaser_email = models.EmailField()
    purchaser_phone_number = models.CharField(max_length=20)
    purchaser_street_address1 = models.CharField(max_length=80)
    purchaser_street_address2 = models.CharField(max_length=80)
    purchaser_town_or_city = models.CharField(max_length=40)
    purchaser_postcode = models.CharField(max_length=20)
    purchaser_county = models.CharField(max_length=20)
    purchaser_country = CountryField(blank_label='Country')

    # License information
    purchase_date = models.DateField(auto_now_add=True)
    no_of_licenses_purchased = models.PositiveSmallIntegerField(default=0)
    purchase_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_number = models.UUIDField(
        primary_key=False,
        default=uuid.uuid4,
        editable=False
    )

    # Stripe-oriented info
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=""
    )

    def __str__(self):
        """
        Returns folio name when called
        """
        return (
            f"{self.purchaser_email} {self.purchase_date}"
        )
