"""
Views relating to the skills section of folios within suite
"""

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse
)
from django.contrib.auth.decorators import login_required
from suite.models import Folio, Skill
from suite.functions import id_has_been_provided
from suite.forms import FolioSkillForm


@login_required
def edit_folio_skills(request, folio_id=None):
    """
    Presents the skills tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        # Get the user's skills
        skills = list(Skill.objects.filter(
            author_id=request.user
        ))

        # For each skill, attach a form to the object
        # And assess whether skill is attached to form
        for skill in skills:
            skill.form = FolioSkillForm(instance=skill)

            # Set is attached to true if folio exists
            # in the skills list of folios
            skill.is_attached = skill.folios.filter(pk=folio_id).exists()

        form = FolioSkillForm()

        context = {
            "folio": folio,
            "form": form,
            "skills": skills
        }

        return render(request, "suite/edit_skills.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def create_folio_skill(request, folio_id):
    """
    Creates a new folio skill
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Create instance of skill form using form data
        form = FolioSkillForm(request.POST)

        # If form is valid
        if form.is_valid():

            # Partially save the form, as author_id
            # will need to be provided
            skill = form.save(commit=False)

            # Save current user as author of skill
            skill.author_id = request.user

            # Fully save skill
            skill.save()

            # Return to folio skill page using folio id
            return redirect(
                reverse("edit_folio_skills",
                        kwargs={"folio_id": folio_id})
            )


@login_required
def update_folio_skill(request, skill_id, folio_id):
    """
    Updates an existing folio skill
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get current skill
        skill_in_db = get_object_or_404(Skill, pk=skill_id)

        # Save instance of skill form
        form = FolioSkillForm(request.POST, instance=skill_in_db)

        # Save form if valid
        if form.is_valid():
            form.save()

        # Return to folio skill page using folio id
        return redirect(
            reverse("edit_folio_skills",
                    kwargs={"folio_id": folio_id})
        )


@login_required
def delete_folio_skill(request, skill_id, folio_id):
    """
    Deletes a user's folio skill
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get the skill
        skill_in_db = get_object_or_404(Skill, pk=skill_id)

        # Delete the skill from the database
        skill_in_db.delete()

        # Return to folio skill page using folio id
        return redirect(
            reverse("edit_folio_skills",
                    kwargs={"folio_id": folio_id})
        )
