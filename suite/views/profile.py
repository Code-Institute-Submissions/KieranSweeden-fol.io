"""
Views relating to the profile section of folios within suite
"""

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from suite.models import Folio
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

        form = FolioProfileForm()

        context = {
            "folio": folio,
            "form": form
        }

        return render(request, "suite/edit_profile.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")
