"""
Models related to the suite & folios within the application
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Folio(models.Model):
    """
    The folio, linking together various
    portfolio snippets, containing user
    information and details related
    to each respective folio.
    """

    # If author is deleted, remove the author's folios
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Date related fields
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    # Folio-oriented details - name is required
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    tagline = models.CharField(max_length=80, null=True, blank=True)

    # Profile information
    current_project_link = models.URLField(null=True, blank=True)
    current_project_desc = models.TextField(null=True, blank=True)
    future_goal = models.TextField(null=True, blank=True)

    # Contact information
    contact_email = models.EmailField(max_length=30, null=True, blank=True)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    contact_github_profile = models.URLField(null=True, blank=True)
    contact_linkedin_profile = models.URLField(null=True, blank=True)

    # Method to return name of folio
    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Project snippet, storing information
    regarding a user's personal project which
    is presented within the project tab
    within a user's folio.
    """

    # If author is deleted, remove the author's folios
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # If Folio is deleted, project snippets persists
    folios = models.ManyToManyField(Folio)

    # Project details
    project_title = models.CharField(max_length=50)
    project_description = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    tech_list = models.CharField(max_length=50)
    github_link = models.URLField(null=True, blank=True)
    live_link = models.URLField(null=True, blank=True)

    # Date related fields
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    # Method to return title of project
    def __str__(self):
        return self.project_title


class Skill(models.Model):
    """
    Skill snippet, storing information regarding
    a user's particular skill which is presented within
    the skills tab of a user's folio
    """

    # If author is deleted, remove the author's folios
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # If Folio is deleted, project snippets persists
    folios = models.ManyToManyField(Folio)

    # Initialise skill types
    class SkillTypes(models.TextChoices):
        """
        List of skill types
        """
        TECH = 'TECH', _('Tech Skill')
        SOFT = 'SOFT', _('Soft Skill')

    # Skill details
    skill_type = models.CharField(
        max_length=4,
        choices=SkillTypes.choices,
        default=SkillTypes.TECH,
    )

    skill_title = models.CharField(max_length=50)
    skill_description = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # Date related fields
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    # Method to return title of project
    def __str__(self):
        return self.skill_title


class Profile(models.Model):
    """
    Profile snippet, storing information regarding
    a user's background and story with the
    software development industry
    """

    # If author is deleted, remove the author's folios
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # If Folio is deleted, project snippets persists
    folios = models.ManyToManyField(Folio)

    # Profile specific fields
    profile_title = models.CharField(max_length=50)
    profile_bio = models.TextField()

    # Date related fields
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    # Method to return title of project
    def __str__(self):
        return self.profile_title
