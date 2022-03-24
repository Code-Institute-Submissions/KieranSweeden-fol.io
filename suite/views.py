"""
Views for the pages related to the folio suite
"""

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from suite.models import Folio


@login_required
def open_suite(request, folio_id):
    """
    This view attempts to direct the user to
    the suite. If a folio id has not been provided,
    the user will be directed to the select folio view.
    Else they'll be directed to the suite viewing folio.
    """

    # Assess whether folio_id has been provided
    if folio_id:
        # If it has, direct the user to folio view
        # attaching the folio id as an argument
        # return redirect('view_folio_projects', folio_id=folio_id)
        return redirect(reverse("view_folio_projects",
                                kwargs={"folio_id": folio_id}))

    else:
        # If one hasn't  been provided
        return redirect("select_folio")


@login_required
def select_folio(request):
    """
    If a folio has not been selected when
    entering the suite, this view will prompt
    the user to select a folio from their library,
    """

    # Get the users folios
    folios = Folio.objects.filter(
        author_id=request.user
    )

    context = {
        "folios": folios
    }

    return render(request, "suite/select_folio.html", context=context)


@login_required
def view_folio_projects(request, folio_id):
    """
    Presents the projects tab of the
    folio to the user.
    """

    return render(request, "suite/edit_projects.html")


@login_required
def view_folio_skills(request):
    """
    Presents the skills tab of the
    folio to the user.
    """

    return render(request, "suite/edit_skills.html")


@login_required
def view_folio_profile(request):
    """
    Presents the profile tab of the
    folio to the user.
    """

    return render(request, "suite/edit_profile.html")

@login_required
def view_folio_contact(request):
    """
    Presents the contact tab of the
    folio to the user.
    """

    return render(request, "suite/edit_contact.html")

