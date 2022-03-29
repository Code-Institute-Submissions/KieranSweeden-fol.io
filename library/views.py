"""
Views for the pages related to the user's folio library
"""

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required

from account.models import UserAccount
from .forms import CreateFolioForm
from suite.models import Folio
from django.contrib.auth.models import User

# Create your views here.


@login_required
def view_library(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    # Get the user's folios
    folios = Folio.objects.filter(
        author_id=request.user
    )

    form = CreateFolioForm()

    context = {
        "form": form,
        "folios": folios
    }

    return render(request, "library/view_library.html", context=context)


@login_required
def create_folio(request):
    """
    Creates a brand new folio when called
    """

    # If the request is post
    if request.method == "POST":

        form = CreateFolioForm(request.POST)

        # If form is valid, save & send success message
        if form.is_valid():
            
            # Partially save the form, as author_id
            # will need to be provided
            folio = form.save(commit=False)

            # Apply current user to author_id
            folio.author_id = request.user
            
            # Save the newly created folio
            folio.save()
    
    # Direct user to page depending on which
    # button they selected
    if "submit_only" in request.POST:

        return redirect("view_library")
    
    elif "submit_and_suite" in request.POST:

        response = redirect(reverse("edit_folio_projects",
                            kwargs={"folio_id": folio.id}))

        response.set_cookie("latest_folio", folio.id)

        return response


@login_required
def update_folio(request, folio_id):
    """
    Updates an existing folio when called
    """

    # Get the folio using the folio id provided
    folio_in_db = get_object_or_404(Folio, pk=folio_id)

    # If the request is post
    if request.method == "POST":
        
        form = CreateFolioForm(request.POST, instance=folio_in_db)

        # If the form is valid
        if form.is_valid():

            # Save the updated form
            form.save()

            return redirect("view_library")
    else:

        form = CreateFolioForm(instance=folio_in_db)

        context = {
            "form": form,
            "folio": folio_in_db
        }

        return render(request, "library/update_folio.html", context=context)


@login_required
def delete_folio(request, folio_id):
    """
    Deletes a user's folio when called
    """

    # Get the folio using the folio id provided
    folio = get_object_or_404(Folio, pk=folio_id)

    # Delete the folio
    folio.delete()

    # Redirect the user to the view library page
    return redirect("view_library")
