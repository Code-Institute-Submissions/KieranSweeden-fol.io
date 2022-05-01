"""
This file contains a basic form that's
used when a user wants to send a
message to the author of a folio.
"""

from django import forms


class SendAuthorMessageForm(forms.Form):
    """
    This form contains the fields required
    to send a message to a folio author.
    """

    # Sender information
    sender_email = forms.CharField(label="Your Name", max_length=30)

    # Message information
    subject = forms.CharField(
        label="Subject",
        max_length=30
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        max_length=250
    )
