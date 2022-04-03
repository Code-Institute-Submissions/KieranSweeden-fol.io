"""
Views relating to the profile section of folios within suite
"""

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse
)
from django.contrib.auth.decorators import login_required
from suite.models import Folio, Profile
from suite.functions import id_has_been_provided
from suite.forms import FolioProfileForm


@login_required
def edit_folio_profile(request, folio_id=None):
    """
    Presents the profile tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        # Get the user's profiles
        profiles = list(Profile.objects.filter(
            author_id=request.user
        ))

        # For each profile, attach a form to the object
        # And assess whether profile is attached to form
        for profile in profiles:
            profile.form = FolioProfileForm(instance=profile)

            # Set is_attached to true if folio exists
            # in the profiles list of folios
            profile.is_attached = profile.folios.filter(pk=folio_id).exists()

        create_profile_form = FolioProfileForm()

        context = {
            "folio": folio,
            "create_profile_form": create_profile_form,
            "profiles": profiles
        }

        return render(request, "suite/edit_profile.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def create_folio_profile(request, folio_id):
    """
    Creates a new folio profile
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Create instance of profile form using form data
        form = FolioProfileForm(request.POST)

        # If form is valid
        if form.is_valid():

            # Partially save the form, as author_id
            # will need to be provided
            profile = form.save(commit=False)

            # Save current user as author of profile
            profile.author_id = request.user

            # Fully save profile
            profile.save()

            # Return to folio profile page using folio id
            return redirect(
                reverse("edit_folio_profile",
                        kwargs={"folio_id": folio_id})
            )
