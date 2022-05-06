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
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from suite.models import Folio, Profile
from suite.functions import (
    id_has_been_provided,
    sort_by_id,
    user_is_author_of_snippet,
    user_is_author_of_folio
)
from suite.forms import FolioProfileForm, FolioProfileCurrentAndFutureGoalForm


@login_required
def edit_folio_profile(request, folio_id=None):
    """
    Presents the profile tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):
        folio = get_object_or_404(Folio, pk=folio_id)

        profiles = list(Profile.objects.filter(
            author_id=request.user
        ))

        for profile in profiles:
            profile.form = FolioProfileForm(
                instance=profile,
                prefix=f"profile-{profile.id}"
            )
            profile.is_attached = profile.folios.filter(pk=folio_id).exists()

        create_profile_form = FolioProfileForm()
        current_and_future_goal_form = FolioProfileCurrentAndFutureGoalForm(
            instance=folio
        )

        context = {
            "folio": folio,
            "create_profile_form": create_profile_form,
            "current_and_future_goal_form": current_and_future_goal_form,
            "profiles": profiles
        }
        return render(request, "suite/edit_profile.html", context=context)

    else:
        return redirect("select_folio")


@login_required
def create_folio_profile(request, folio_id):
    """
    Creates a new folio profile
    """

    if request.method == "POST":
        form = FolioProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.author_id = request.user
            profile.save()
            messages.success(
                request,
                f"The {profile.profile_title} About Me has "
                f"been successfully created."
            )

        else:
            messages.error(
                request,
                "Data posted was not valid "
                "to create a new profile."
            )

    else:
        messages.error(
            request,
            "Data should be posted when "
            "attempting to create a new profile."
        )

    return redirect(
        reverse("edit_folio_profile",
                kwargs={"folio_id": folio_id})
    )


@login_required
def update_folio_profile(request, profile_id, folio_id):
    """
    Updates an existing folio profile
    """

    if user_is_author_of_snippet(request.user, 'profile', profile_id):

        if request.method == "POST":
            profile = get_object_or_404(Profile, pk=profile_id)
            post = request.POST.copy()
            for key, value in request.POST.items():
                prefix_removed_name = key.replace(f"profile-{profile.id}-", "")
                post[prefix_removed_name] = value

            form = FolioProfileForm(post, instance=profile)

            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    f"The {profile.profile_title} About Me has "
                    f"been successfully updated."
                )

            else:
                messages.error(
                    request,
                    "Data posted was not valid "
                    "to update a profile."
                )
        else:
            messages.error(
                request,
                "Data should be posted when "
                "attempting to update a profile."
            )

        return redirect(
            reverse("edit_folio_profile",
                    kwargs={"folio_id": folio_id})
        )

    else:
        messages.error(
            request,
            "You cannot interact with "
            "profile snippets that are not your own."
        )
        return redirect("view_library")


@login_required
def update_profiles_attached_to_folio(request, folio_id):
    """
    Updates which profiles are attached
    to the currently viewed folio
    """

    if user_is_author_of_folio(request.user, folio_id):

        if request.method == "POST":
            data = json.loads(request.body)
            list_of_profiles = data['profiles']
            list_of_profiles.sort(reverse=False, key=sort_by_id)

            profiles_in_db = Profile.objects.filter(
                id__in=[profile['id'] for profile in list_of_profiles]
            )
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

                    messages.success(
                        request,
                        f"The profile snippets attached to {folio.name} "
                        f"have been updated successfully."
                    )

                else:
                    print(
                        "DEBUG: Profile id's didn't match, "
                        "likely sorting error"
                    )

            return HttpResponse("OK")

        else:
            raise exceptions.BadRequest

    else:
        raise exceptions.PermissionDenied


@login_required
def update_current_and_future_goal(request, folio_id):
    """
    Updates the current project and future goal
    portion of folio that's presented within the
    profile tab in the suite.
    """

    if user_is_author_of_folio(request.user, folio_id):

        if request.method == "POST":
            folio = get_object_or_404(Folio, pk=folio_id)

            form = FolioProfileCurrentAndFutureGoalForm(
                request.POST,
                instance=folio
            )

            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    f"Current & future goals within {folio.name} "
                    f"have been updated successfully."
                )
            else:
                messages.error(
                    request,
                    "Data posted was not valid "
                    "to update current project & future goal."
                )
        else:
            messages.error(
                request,
                "Data should be posted when "
                "attempting to update your "
                "current project and future goal."
            )

        return redirect(reverse(
            "edit_folio_profile",
            kwargs={"folio_id": folio_id}
        ))

    else:
        messages.error(
            request,
            "You cannot interact with content within "
            "folios that are not your own."
        )
        return redirect("view_library")


@login_required
def delete_folio_profile(request, profile_id, folio_id):
    """
    Deletes a user's folio profile
    """

    if user_is_author_of_snippet(request.user, 'profile', profile_id):
    
        if request.method == "POST":
            profile_in_db = get_object_or_404(Profile, pk=profile_id)
            profile_in_db.delete()
            messages.success(
                request,
                f"The {profile_in_db.profile_title} About Me profile "
                f"has been deleted successfully."
            )
        
        else:
            messages.error(
                request,
                "A delete command should "
                "be sent as a POST request."
            )

        return redirect(
            reverse("edit_folio_profile",
                    kwargs={"folio_id": folio_id})
        )
    
    else:
        messages.error(
            request,
            "You cannot delete profile snippets "
            "that are not your own."
        )
        return redirect("view_library")
