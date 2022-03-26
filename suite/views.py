"""
Views for the pages related to the folio suite
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from suite.models import Folio
from suite.functions import id_has_been_provided


@login_required
def open_suite(request, folio_id):
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
        return redirect(reverse("view_folio_projects",
                                kwargs={"folio_id": folio_id}))

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

        # Direct user to suite using folio_id
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


@login_required
def edit_folio_projects(request, folio_id=None):
    """
    Presents the projects tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_projects.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def edit_folio_skills(request, folio_id=None):
    """
    Presents the skills tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_skills.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def edit_folio_profile(request, folio_id=None):
    """
    Presents the profile tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_profile.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def edit_folio_contact(request, folio_id=None):
    """
    Presents the contact tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_contact.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")
