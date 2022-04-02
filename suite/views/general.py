"""
Views for general functionality regarding suite
"""

from django.shortcuts import (
    render,
    redirect,
    reverse
)
from django.contrib.auth.decorators import login_required
from suite.models import Folio
from suite.functions import id_has_been_provided, user_is_author_of_folio


@login_required
def open_suite(request, folio_id=None):
    """
    This view attempts to direct the user to
    the suite. If a folio id has not been provided,
    the user will be directed to the select folio view.
    Else they'll be directed to the suite viewing folio.
    """

    # Assess whether folio_id has been provided
    if id_has_been_provided(folio_id):
        # If it has, direct the user to folio view
        # attaching the folio id as an argument
        # return redirect('view_folio_projects', folio_id=folio_id)

        # Create response object to redirect user
        response = redirect(reverse("edit_folio_projects",
                            kwargs={"folio_id": folio_id}))

        # Store folio_id in cookies
        response.set_cookie("latest_folio", folio_id)

        return response

    # With no folio_if provided, check the user's latest folio cookie
    elif request.COOKIES.get('latest_folio') is not None:

        # Grab the folio_id given the cookie exists
        folio_id = request.COOKIES.get('latest_folio')

        # Check the user is actually the author of the folio
        if user_is_author_of_folio(request.user, folio_id):

            # Open folio if true
            return redirect(reverse("edit_folio_projects",
                                    kwargs={"folio_id": folio_id}))

    # If folio_id checks are all false, direct user to select folio page
    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def select_folio(request):
    """
    If a folio has not been selected when
    entering the suite, this view will prompt
    the user to select a folio from their library,
    """

    if request.method == "POST":

        # Get the id from request
        folio_id = request.POST.get('folio_selected')

        # Create response object to redirect user
        response = redirect(reverse("edit_folio_projects",
                            kwargs={"folio_id": folio_id}))

        # Store folio_id in cookies
        response.set_cookie("latest_folio", folio_id)

        return response

    else:

        # Check the user's cookies for latest folio
        if request.COOKIES.get('latest_folio') is not None:

            # Grab the folio_id given the cookie exists
            folio_id = request.COOKIES.get('latest_folio')

            # Check the user is actually the author of the folio
            if user_is_author_of_folio(request.user, folio_id):

                # Open folio if true
                return redirect(reverse("edit_folio_projects",
                                        kwargs={"folio_id": folio_id}))

        else:

            # Get the users folios
            folios = Folio.objects.filter(
                author_id=request.user
            )

            context = {
                "folios": folios
            }

            return render(request, "suite/select_folio.html", context=context)
