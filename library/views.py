"""
Views for the pages related to the user's folio library
"""

from django.shortcuts import render, get_object_or_404, redirect
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

    # Get folios
    folios = Folio.objects.filter(
        author_id=request.user
    )

    print(folios)

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
    
    return redirect("view_library")
