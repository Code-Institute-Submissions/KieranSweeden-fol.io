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
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    current_project_link = models.URLField(null=True, blank=True)
    current_project_desc = models.TextField(null=True, blank=True)
    future_goal = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def toggle_published_state(self):
        """
        Toggle's the folio's published state
        """
        self.is_published = not self.is_published
        self.save()

    def __str__(self):
        """
        Returns folio name when called
        """
        return self.name


class Project(models.Model):
    """
    Project snippet, storing information
    regarding a user's personal project which
    is presented within the project tab
    within a user's folio.
    """
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    folios = models.ManyToManyField(Folio)
    project_title = models.CharField(max_length=30)
    project_description = models.TextField(max_length=300)
    tech_list = models.CharField(max_length=50)
    github_link = models.URLField(null=True, blank=True)
    live_link = models.URLField(null=True, blank=True)
    image = models.ImageField(
        upload_to="projects",
        null=True,
        blank=True
    )
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.project_title


class Skill(models.Model):
    """
    Skill snippet, storing information regarding
    a user's particular skill which is presented within
    the skills tab of a user's folio
    """
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    folios = models.ManyToManyField(Folio)

    class SkillTypes(models.TextChoices):
        """
        List of skill types
        """
        TECH = 'TECH', _('Tech Skill')
        SOFT = 'SOFT', _('Soft Skill')

    skill_type = models.CharField(
        max_length=4,
        choices=SkillTypes.choices,
        default=SkillTypes.TECH,
    )
    skill_title = models.CharField(max_length=20)
    skill_description = models.TextField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.skill_title


class Profile(models.Model):
    """
    Profile snippet, storing information regarding
    a user's background and story with the
    software development industry
    """
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    folios = models.ManyToManyField(Folio)
    profile_title = models.CharField(max_length=20)
    profile_bio = models.TextField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.profile_title
