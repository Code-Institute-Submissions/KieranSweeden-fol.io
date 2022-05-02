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

    sender_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "e.g. kathleenbooth@email.com"
            }),
        label="Your Email Address",
        max_length=30
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. I'd like to collaborate..."
        }),
        label="Subject Of Message",
        max_length=30
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            "placeholder": "e.g. I'd like to discuss..."
        }),
        label="Message Content",
        max_length=250
    )
