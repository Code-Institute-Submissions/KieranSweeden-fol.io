"""
Views relating to the profile section of folios within suite
"""

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
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
