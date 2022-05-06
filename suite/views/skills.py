"""
Views relating to the skills section of folios within suite
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
from suite.models import Folio, Skill
from suite.functions import (
    id_has_been_provided,
    is_tech_skill,
    is_soft_skill,
    sort_by_id,
    user_is_author_of_snippet,
    user_is_author_of_folio
)
from suite.forms import FolioSkillForm


@login_required
def edit_folio_skills(request, folio_id=None):
    """
    Presents the skills tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):
        folio = get_object_or_404(Folio, pk=folio_id)

        skills = list(Skill.objects.filter(
            author_id=request.user
        ))

        for skill in skills:
            skill.form = FolioSkillForm(
                instance=skill,
                prefix=f"skill-{skill.id}"
            )
            skill.is_attached = skill.folios.filter(pk=folio_id).exists()

        tech_skills = list(filter(is_tech_skill, skills))
        soft_skills = list(filter(is_soft_skill, skills))

        form = FolioSkillForm()
        context = {
            "folio": folio,
            "form": form,
            "tech_skills": tech_skills,
            "soft_skills": soft_skills
        }

        return render(request, "suite/edit_skills.html", context=context)

    else:
        return redirect("select_folio")


@login_required
def create_folio_skill(request, folio_id):
    """
    Creates a new folio skill
    """

    if request.method == "POST":
        form = FolioSkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.author_id = request.user
            skill.save()
            messages.success(
                request,
                f"The {skill.skill_title} skill has "
                f"been created successfully."
            )
            return redirect(
                reverse("edit_folio_skills",
                        kwargs={"folio_id": folio_id})
            )


@login_required
def update_folio_skill(request, skill_id, folio_id):
    """
    Updates an existing folio skill
    """

    if request.method == "POST":
        skill = get_object_or_404(Skill, pk=skill_id)

        post = request.POST.copy()
        for key, value in request.POST.items():
            prefix_removed_name = key.replace(f"skill-{skill.id}-", "")
            post[prefix_removed_name] = value

        form = FolioSkillForm(post, instance=skill)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"The {skill.skill_title} skill "
                f"has been updated successfully."
            )

        return redirect(
            reverse("edit_folio_skills",
                    kwargs={"folio_id": folio_id})
        )


@login_required
def update_skills_attached_to_folio(request, folio_id):
    """
    Updates which skills are attached
    to the currently viewed folio
    """

    if request.method == "POST":
        # Retrieve list of project status's sorted by id
        data = json.loads(request.body)
        list_of_skills = data['skills']
        list_of_skills.sort(reverse=False, key=sort_by_id)

        # Grab users skills from DB using ID's provided
        skills_in_db = Skill.objects.filter(
             id__in=[skill['id'] for skill in list_of_skills]
        )

        # Get currently viewed folio
        folio = get_object_or_404(Folio, pk=folio_id)

        # Iterate through skills in db & status's given from user actions
        for skill_in_db, skill_status in zip(skills_in_db, list_of_skills):
            # Ensure ID's match
            if skill_in_db.id == int(skill_status['id']):
                # Add/remove folio or continue based on is_attached
                # status & if the folio already exists in project folios
                if skill_status['is_attached']:
                    if skill_in_db.folios.filter(pk=folio_id).exists():
                        continue
                    else:
                        skill_in_db.folios.add(folio)
                else:
                    if skill_in_db.folios.filter(pk=folio_id).exists():
                        skill_in_db.folios.remove(folio)
                    else:
                        continue
                
                messages.success(
                    request,
                    f"The skills attached to {folio.name} "
                    f"have been updated successfully."
                )

            else:
                print("they didn't match, sorting error")

        # Return an OK response
        return HttpResponse("OK")


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

        messages.success(
            request,
            f"The {skill_in_db.skill_title} skill "
            f"has been deleted successfully."
        )

        # Return to folio skill page using folio id
        return redirect(
            reverse("edit_folio_skills",
                    kwargs={"folio_id": folio_id})
        )
