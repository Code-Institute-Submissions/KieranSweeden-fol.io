"""
Models that relate to the user's account
"""

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserAccount(models.Model):
    """
    A user account that's linked to the
    user's authentication log-in.
    This stores the user's general info &
    default billing information 
    """
    
    # Link to attach user account to specific user
    # A specific user can only have one account
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Default user info
    first_name = models.CharField(
        max_length=20, null=True, blank=True
    )
    last_name = models.CharField(
        max_length=20, null=True, blank=True
    )
    phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    profile_picture = models.ImageField(
        upload_to="profile-pictures",
        null=True,
        blank=True
    )

    # Folio oriented info
    number_of_licenses = models.PositiveSmallIntegerField(default=0)
    github_profile = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)

    # Default billing info
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_country = CountryField(
        blank_label='Country', null=True, blank=True
    )

    def add_licences_to_user_account(self, amount):
        """
        Method increments the user's amount of
        licences provided after a purchase
        """
        self.number_of_licenses += int(amount)
        self.save()
    
    def get_full_name(self):
        """
        Returns the user's first
        and last name as a string
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        When logged via console,
        the user's email will be returned
        """
        return self.user.email


# recieves from the post_save event from the user model
# if new, create new, otherwise save to existing user
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserAccount.objects.create(user=instance)
