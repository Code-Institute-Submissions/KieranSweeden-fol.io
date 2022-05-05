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

        widgets = {
            'project_description': forms.Textarea(attrs={
                'rows': 6
            })
        }

    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        # Setup form as default
        super().__init__(*args, **kwargs)

        # Placeholders
        placeholders = {
            "project_title": "e.g. To-do List",
            "project_description": "e.g. This is a to-do list app that "
            "features the use of the local storage API and...",
            "tech_list": "HTML, CSS, JavaScript",
            "github_link": "https://github.com/...",
            "live_link": "https://...",
            "image": "Project Image"
        }
        labels = {
            "project_title": "Project Title",
            "project_description": "Project Description",
            "tech_list": "Technology List (seperated by commas)",
            "github_link": "GitHub Repository Link",
            "live_link": "Live Deployment Link",
            "image": "Project Image"
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
            if field != 'image':
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholders[field]


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

        widgets = {
            'skill_description': forms.Textarea(attrs={
                'rows': 6
            })
        }

    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        super().__init__(*args, **kwargs)

        placeholders = {
            "skill_title": "e.g. Python",
            "skill_description": "e.g. Examples using Python include "
            "making use of frameworks such as Flask and Djano...",
            "skill_type": "Skill type"
        }
        labels = {
            "skill_title": "Skill Title",
            "skill_description": "Skill Description",
            "skill_type": "Skill Type"
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
            if field != 'skill_type':
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholders[field]


class FolioProfileForm(forms.ModelForm):
    """
    This form relates to the profile model and
    is the form the user submits to regarding
    folio profiles
    """

    class Meta:
        model = Profile
        fields = [
            "profile_title",
            "profile_bio"
        ]
        widgets = {
            'profile_bio': forms.Textarea(attrs={
                'rows': 6
            })
        }

    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        super().__init__(*args, **kwargs)

        placeholders = {
            "profile_title": "e.g. Self Teaching",
            "profile_bio": "e.g. My journey with web development "
            "began with learning the HTML and CSS on the side "
            "whilst working full-time..."
        }
        labels = {
            "profile_title": "Profile Title",
            "profile_bio": "Profile Bio"
        }

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[
                field
            ]
            self.fields[field].label = labels[field]


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

        widgets = {
            'current_project_desc': forms.Textarea(attrs={
                'rows': 5
            }),
            'future_goal': forms.Textarea(attrs={
                'rows': 3
            })
        }

    # Customize form
    def __init__(self, *args, **kwargs):
        """
        Insert placeholders
        """

        # Setup form as default
        super().__init__(*args, **kwargs)

        # Placeholders
        placeholders = {
            "current_project_link": "https://...",
            "current_project_desc": "e.g. The project I'm currently working "
            "on is a MERN project that aims to solve the problem of...",
            "future_goal": "e.g. Within the next few years I'd like"
            "to continue progressing with my front-end development..."
        }
        labels = {
            "current_project_link": "Current Project Link",
            "current_project_desc": "Current Project Description",
            "future_goal": "Your Future Goals"
        }

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[
                field
            ]
            self.fields[field].label = labels[field]
