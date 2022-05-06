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
from suite.functions import user_is_author_of_folio
from account.models import UserAccount
from .forms import CreateFolioForm


@login_required
def view_library(request):
    """
    Collects the user's list of folios, adds a form to each
    so they can be updated and presents them within library page
    """

    folios = Folio.objects.filter(
        author_id=request.user
    ).order_by(
        '-date_created'
    )

    for folio in folios:
        folio.form = CreateFolioForm(
            instance=folio,
            prefix=f"folio-{folio.id}"
        )

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
    Creates a brand new folio with provided data when called
    """

    if request.method == "POST":

        form = CreateFolioForm(request.POST)

        if form.is_valid():
            folio = form.save(commit=False)
            folio.author_id = request.user
            folio.save()

            messages.success(
                request,
                f"{folio.name} has been created successfully."
            )

            if "submit_and_suite" in request.POST:
                response = redirect(reverse("edit_folio_projects",
                                    kwargs={"folio_id": folio.id}))
                response.set_cookie("latest_folio", folio.id)
                return response

            else:
                return redirect("view_library")

        else:
            messages.error(
                request,
                "The data you've provided to"
                "create a folio is invalid."
            )
            return redirect("view_library")
    else:
        messages.error(
            request,
            "Necessary folio data needs to posted "
            "in order to create a folio."
        )
        return redirect("view_library")


@login_required
def update_folio(request, folio_id):
    """
    Updates an existing folio when called
    """

    if user_is_author_of_folio(request.user, folio_id):
        folio_in_db = get_object_or_404(Folio, pk=folio_id)

        if request.method == "POST":
            post = request.POST.copy()
            post['name'] = post[f"folio-{folio_id}-name"]
            post['description'] = post[f"folio-{folio_id}-description"]
            form = CreateFolioForm(post, instance=folio_in_db)

            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    f"{folio_in_db.name} has been updated successfully."
                )

                if "submit_and_suite" in request.POST:
                    response = redirect(reverse("edit_folio_projects",
                                        kwargs={"folio_id": folio_id}))
                    response.set_cookie("latest_folio", folio_id)
                    return response

                else:
                    return redirect("view_library")

            else:
                messages.error(
                    request,
                    f"The changes made to {folio_in_db} were invalid."
                )
                return redirect("view_library")

        else:
            messages.error(
                request,
                "Data should be sent when "
                "attempting to update a folio."
            )
            return redirect("view_library")

    else:
        messages.error(
            request,
            "You cannot interact with "
            "folios that are not your own."
        )
        return redirect("view_library")


@login_required
def toggle_folio_published_state(request, folio_id):
    """
    If folio is already published, it is toggled to false.
    If not, depending on the amount of licenses the user holds,
    either publish the selected folio or direct user to
    purchase more licenses.
    """

    if user_is_author_of_folio(request.user, folio_id):
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

            if user_account.number_of_licenses == 0:

                messages.warning(
                    request,
                    "You need to purchase a license "
                    "before you can publish a folio."
                )
                return redirect("purchase_license")

            else:
                amount_of_published_folios = len(Folio.objects.filter(
                    author_id=request.user
                ).filter(
                    is_published=True
                ))

                if amount_of_published_folios < \
                   user_account.number_of_licenses:
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
                        "Please purchase additional "
                        "licenses to publish more folios."
                    )
                    return redirect("purchase_license")

    else:
        messages.warning(
            request,
            "You cannot interact with "
            "folios that are not your own."
        )
        return redirect("view_library")


@login_required
def delete_folio(request, folio_id):
    """
    Deletes a user's folio when called &
    removes it from the latest folio cookie
    if it's the last folio visited
    """

    if user_is_author_of_folio(request.user, folio_id):
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

    else:
        messages.warning(
            request,
            "You cannot interact with "
            "folios that are not your own."
        )
        return redirect("view_library")
