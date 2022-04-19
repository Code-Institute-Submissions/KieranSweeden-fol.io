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
            "live_link"
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
            "project_title": "Project title",
            "project_description": "Project description",
            "tech_list": "Technology list (seperated by commas)",
            "github_link": "GitHub repository link",
            "live_link": "Live deployment link"
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


class FolioContactForm(forms.ModelForm):
    """
    This form relates to the contact information
    within the folio model.
    """

    class Meta:
        # Meta options inform django what model
        # this class will be associated with
        model = Folio

        # Explicity telling django to only
        # load the fields relating to the folio's
        # contact information
        fields = [
            'contact_email',
            'contact_number',
            'contact_github_profile',
            'contact_linkedin_profile'
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
            'contact_email': 'Email address',
            'contact_number': 'Phone number',
            'contact_github_profile': 'GitHub profile URL',
            'contact_linkedin_profile': 'LinkedIn profile URL'
        }

        # Auto focus on the first field
        self.fields['contact_email'].widget.attrs['autofocus'] = True

        # Iterate over the fields, inserting
        # placeholders along the way
        for field in self.fields:

            # Give them their respective placeholders & classes
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = placeholder
