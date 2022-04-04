"""
Views relating to the profile section of folios within suite
"""

import json
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
    HttpResponse
)
from django.contrib.auth.decorators import login_required
from suite.models import Folio, Profile
from suite.functions import id_has_been_provided, sort_by_id
from suite.forms import FolioProfileForm, FolioProfileCurrentAndFutureGoalForm


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

        current_and_future_goal_form = FolioProfileCurrentAndFutureGoalForm()

        context = {
            "folio": folio,
            "create_profile_form": create_profile_form,
            "current_and_future_goal_form": current_and_future_goal_form,
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


@login_required
def update_folio_profile(request, profile_id, folio_id):
    """
    Updates an existing folio profile
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get current profile
        profile_in_db = get_object_or_404(Profile, pk=profile_id)

        # Save instance of profile form
        form = FolioProfileForm(request.POST, instance=profile_in_db)

        # Save form if valid
        if form.is_valid():
            form.save()

        # Return to folio profile page using folio id
        return redirect(
            reverse("edit_folio_profile",
                    kwargs={"folio_id": folio_id})
        )


@login_required
def update_profiles_attached_to_folio(request, folio_id):
    """
    Updates which profiles are attached
    to the currently viewed folio
    """

    if request.method == "POST":
        # Retrieve list of project status's sorted by id
        data = json.loads(request.body)
        list_of_profiles = data['profiles']
        list_of_profiles.sort(reverse=False, key=sort_by_id)

        # Grab users profiles from DB using ID's provided
        profiles_in_db = Profile.objects.filter(
             id__in=[profile['id'] for profile in list_of_profiles]
        )

        # Get currently viewed folio
        folio = get_object_or_404(Folio, pk=folio_id)

        # Iterate through profiles in db & status's given from user actions
        for profile_in_db, profile_status in zip(profiles_in_db,
                                                 list_of_profiles):
            # Ensure ID's match
            if profile_in_db.id == int(profile_status['id']):
                # Add/remove folio or continue based on is_attached
                # status & if the folio already exists in project folios
                if profile_status['is_attached']:
                    if profile_in_db.folios.filter(pk=folio_id).exists():
                        continue
                    else:
                        profile_in_db.folios.add(folio)
                else:
                    if profile_in_db.folios.filter(pk=folio_id).exists():
                        profile_in_db.folios.remove(folio)
                    else:
                        continue
            else:
                print("they didn't match, sorting error")

        # Return an OK response
        return HttpResponse("OK")


@login_required
def delete_folio_profile(request, profile_id, folio_id):
    """
    Deletes a user's folio profile
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get the profile
        profile_in_db = get_object_or_404(Profile, pk=profile_id)

        # Delete the profile from the database
        profile_in_db.delete()

        # Return to folio profile page using folio id
        return redirect(
            reverse("edit_folio_profile",
                    kwargs={"folio_id": folio_id})
        )
