"""
This file contains various forms that relate
to the folio model
"""

from django import forms
from .models import (
    Folio,
    Project,
    Skill,
    Profile
)


class FolioProjectForm(forms.ModelForm):
    """
    This form relates to the project model and
    is the form the user submits to change
    a project.
    """

    class Meta:
        # Associated with Project model
        model = Project

        # Include fields that are editable
        fields = [
            "project_title",
            "project_description",
            "tech_list",
            "github_link",
            "live_link",
            "image"
        ]
    
    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        # Setup form as default
        super().__init__(*args, **kwargs)

        # Placeholders
        placeholders = {
            "project_title": "Project Title",
            "project_description": "Project Description",
            "tech_list": "Technology List (seperated by commas)",
            "github_link": "GitHub Repository Link",
            "live_link": "Live Deployment Link",
            "image": "Project Image"
        }

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = placeholder


class FolioSkillForm(forms.ModelForm):
    """
    This form relates to the skill model and
    is the form the user submits to regarding skills
    """

    class Meta:
        # Associated with Project model
        model = Skill

        # Include fields that are editable
        fields = [
            "skill_title",
            "skill_description",
            "skill_type"
        ]

    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        # Setup form as default
        super().__init__(*args, **kwargs)

        # Placeholders
        placeholders = {
            "skill_title": "Skill title",
            "skill_description": "Skill description",
            "skill_type": "Skill type"
        }

        # Iterate over the fields, inserting
        # placeholders & labels along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = placeholder


class FolioProfileForm(forms.ModelForm):
    """
    This form relates to the profile model and
    is the form the user submits to regarding
    folio profiles
    """

    class Meta:
        # Associated with Project model
        model = Profile

        # Include fields that are editable
        fields = [
            "profile_title",
            "profile_bio"
        ]

    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        # Setup form as default
        super().__init__(*args, **kwargs)

        # Placeholders
        placeholders = {
            "profile_title": "Profile title",
            "profile_bio": "Biography (What's presented within the folio)"
        }

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:
            # Give them their respective placeholders & classes
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = placeholder


class FolioProfileCurrentAndFutureGoalForm(forms.ModelForm):
    """
    This form relates to the folio model and
    is the form the user submits to regarding
    their current projects & future goals
    """

    class Meta:
        # Associated with Project model
        model = Folio

        # Include fields that are editable
        fields = [
            "current_project_link",
            "current_project_desc",
            "future_goal"
        ]

    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        # Setup form as default
        super().__init__(*args, **kwargs)

        # Placeholders
        placeholders = {
            "current_project_link": "Current project link",
            "current_project_desc": "Current project description",
            "future_goal": "Insert your future goals"
        }

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = placeholder
