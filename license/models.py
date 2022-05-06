"""
Models related to the license store
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from django_countries.fields import CountryField

import uuid


class LicensePurchase(models.Model):
    """
    A license purchase which gets created
    when a user makes license purchase
    via the license store & stripe
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    purchaser_full_name = models.CharField(max_length=40)
    purchaser_email = models.EmailField()
    purchaser_phone_number = models.CharField(max_length=20)
    purchaser_street_address1 = models.CharField(max_length=80)
    purchaser_street_address2 = models.CharField(max_length=80)
    purchaser_town_or_city = models.CharField(max_length=40)
    purchaser_postcode = models.CharField(max_length=20)
    purchaser_county = models.CharField(max_length=20)
    purchaser_country = CountryField(blank_label='Country')

    purchase_date = models.DateField(auto_now_add=True)
    no_of_licenses_purchased = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(50)
        ]
    )

    purchase_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_number = models.UUIDField(
        primary_key=False,
        default=uuid.uuid4,
        editable=False
    )

    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=""
    )

    def __str__(self):
        """
        Returns license purchase email
        and purchase when a license
        purchase is being referred to
        """
        return (
            f"{self.purchaser_email} {self.purchase_date}"
        )
