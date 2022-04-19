"""
Views relating to the contact section of folios within suite
"""

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from suite.models import Folio
from suite.functions import id_has_been_provided
from suite.forms import FolioContactForm


@login_required
def edit_folio_contact(request, folio_id=None):
    """
    Presents the contact tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)
        form = FolioContactForm(instance=folio)

        context = {
            "folio": folio,
            "form": form
        }

        return render(request, "suite/edit_contact.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def update_folio_contact(request, folio_id):
    """
    Updates the user's contact information
    within folio
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get current folio
        folio_in_db = get_object_or_404(Folio, pk=folio_id)

        # Save instance of project form
        form = FolioContactForm(request.POST, instance=folio_in_db)

        # Save form if valid
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"The contact information within {folio_in_db.name} "
                f"has been successfully updated."
            )

        # Return to folio project page using folio id
        return redirect(
            reverse("edit_folio_contact",
                    kwargs={"folio_id": folio_id}))
