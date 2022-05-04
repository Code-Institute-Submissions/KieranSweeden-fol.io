"""
Views for the pages related to the user's folio library
"""

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from suite.models import Folio
from account.models import UserAccount
from .forms import CreateFolioForm


@login_required
def view_library(request):
    """
    Collects the user's list of folios
    and presents them within the library page
    """

    folios = Folio.objects.filter(
        author_id=request.user
    ).order_by(
        '-date_created'
    )

    for folio in folios:
        folio.form = CreateFolioForm(instance=folio)

    user_account = get_object_or_404(
        UserAccount,
        pk=request.user.id
    )

    amount_of_published_folios = len(Folio.objects.filter(
        author_id=request.user
    ).filter(
        is_published=True
    ))

    form = CreateFolioForm()

    context = {
        "form": form,
        "folios": folios,
        "total_licenses": user_account.number_of_licenses,
        "used_licenses": amount_of_published_folios
    }

    return render(request, "library/view_library.html", context=context)


@login_required
def create_folio(request):
    """
    Creates a brand new folio when called
    """

    # If the request is post
    if request.method == "POST":

        print(request.POST)

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

            messages.success(
                request,
                f"{folio.name} has been created successfully."
            )

    # Direct user to page depending on which
    # button they selected
    if "submit_only" in request.POST:

        # Redirect to library
        return redirect("view_library")

    elif "submit_and_suite" in request.POST:

        # Create response
        response = redirect(reverse("edit_folio_projects",
                            kwargs={"folio_id": folio.id}))

        # Set cookie to store the current folio as
        # most recently opened folio
        response.set_cookie("latest_folio", folio.id)

        # Re-direct user
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

            messages.success(
                request,
                f"{folio_in_db.name} has been updated successfully"
            )

            if "update_only" in request.POST:

                return redirect("view_library")

            elif "update_&_suite" in request.POST:

                # Create response
                response = redirect(reverse("edit_folio_projects",
                                    kwargs={"folio_id": folio_id}))

                # Set cookie to store the current folio as
                # most recently opened folio
                response.set_cookie("latest_folio", folio_id)

                # Re-direct user
                return response

        else:
            messages.error(
                request,
                f"The changes made to {folio_in_db} were invalid."
            )

            return redirect("view_library")

    else:
        form = CreateFolioForm(instance=folio_in_db)
        context = {
            "form": form,
            "folio": folio_in_db
        }
        return render(request, "library/update_folio.html", context=context)


@login_required
def toggle_folio_published_state(request, folio_id):
    """
    If folio is already published, it is toggled to false.
    If not, depending on the amount of licenses the user holds,
    either publish the selected folio or direct user to
    purchase more licenses.
    """

    folio = get_object_or_404(Folio, pk=folio_id)

    if folio.is_published:
        folio.toggle_published_state()
        messages.success(
            request,
            f"{folio.name} has been concealed successfully."
        )
        return redirect("view_library")

    else:
        user_account = get_object_or_404(
            UserAccount, pk=request.user.id
        )

        amount_of_published_folios = len(Folio.objects.filter(
            author_id=request.user
        ).filter(
            is_published=True
        ))

        if amount_of_published_folios < user_account.number_of_licenses:
            folio.toggle_published_state()
            messages.success(
                request,
                f"{folio.name} has been published successfully."
            )
            return redirect("view_library")

        else:
            messages.warning(
                request,
                "You have used all of your licenses. "
                "Please purchase additional licenses to publish more folios."
            )
            return redirect("purchase_license")


@login_required
def delete_folio(request, folio_id):
    """
    Deletes a user's folio when called &
    removes it from the latest folio cookie
    if it's the last folio visited
    """

    folio = get_object_or_404(Folio, pk=folio_id)
    folio.delete()

    response = redirect(reverse("view_library"))

    if 'latest_folio' in request.COOKIES.keys():
        latest_folio = request.COOKIES['latest_folio']
        if int(folio_id) == int(latest_folio):
            response.delete_cookie('latest_folio')

    messages.success(
        request,
        f"{folio.name} has been deleted successfully."
    )

    return response
