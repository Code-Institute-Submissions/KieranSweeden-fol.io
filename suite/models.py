"""
Models related to the suite & folios within the application
"""

from django.db import models
from account.models import UserAccount


class Folio(models.Model):
    """
    The folio, linking together various
    portfolio snippets, containing user
    information and details related
    to each respective folio.
    """

    # If author is deleted, remove the author's folios
    author_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    # Date related fields
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    # Folio-oriented details
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    tagline = models.CharField(max_length=80, null=True, blank=True)

    # Profile information
    about_me = models.TextField(null=True, blank=True)
    current_project_link = models.URLField(null=True, blank=True)
    current_project_desc = models.TextField(null=True, blank=True)

    # Contact information
    contact_email = models.EmailField(max_length=30, null=True, blank=True)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    contact_github_profile = models.URLField(null=True, blank=True)
    contact_linkedin_profile = models.URLField(null=True, blank=True)

    # Method to return name of folio
    def __str__(self):
        return self.name
