"""
Views relating to the projects section of folios within suite
"""

import json
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.core import exceptions
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from suite.models import Folio, Project
from suite.functions import (
    id_has_been_provided,
    sort_by_id,
    user_is_author_of_snippet,
    user_is_author_of_folio
)
from suite.forms import FolioProjectForm


@login_required
def edit_folio_projects(request, folio_id=None):
    """
    Presents the projects tab of the
    folio to the user.
    """
    if id_has_been_provided(folio_id):
        folio = get_object_or_404(Folio, pk=folio_id)

        projects = list(Project.objects.filter(
            author_id=request.user
        ))

        for project in projects:
            project.form = FolioProjectForm(
                instance=project,
                prefix=f"project-{project.id}")
            project.is_attached = project.folios.filter(pk=folio_id).exists()

        form = FolioProjectForm()
        context = {
            "folio": folio,
            "projects": projects,
            "form": form
        }

        return render(
            request,
            "suite/edit_projects.html",
            context=context
        )

    else:
        return redirect("select_folio")


@login_required
def create_folio_project(request, folio_id):
    """
    Creates a new folio project
    """

    if request.method == "POST":
        form = FolioProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            project = form.save(commit=False)
            project.author_id = request.user
            project.save()
            messages.success(
                request,
                f"The {project.project_title} project has "
                f"been created successfully."
            )

        else:
            messages.error(
                request,
                "Data posted was not valid "
                "to create a new project."
            )

    else:
        messages.error(
            request,
            "Data should be posted when "
            "attempting to create a new project."
        )

    return redirect(
        reverse("edit_folio_projects",
                kwargs={"folio_id": folio_id})
    )


@login_required
def update_folio_project(request, project_id, folio_id):
    """
    Updates an existing folio project
    """

    if user_is_author_of_snippet(request.user, "project", project_id):

        if request.method == "POST":
            project = get_object_or_404(Project, pk=project_id)
            post = request.POST.copy()
            for key, value in request.POST.items():
                prefix_removed_name = key.replace(f"project-{project.id}-", "")
                post[prefix_removed_name] = value

            files = request.FILES.copy()
            for key, value in request.FILES.items():
                prefix_removed_name = key.replace(f"project-{project.id}-", "")
                files[prefix_removed_name] = value

            form = FolioProjectForm(
                post,
                files,
                instance=project
            )

            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    f"The {project.project_title} project "
                    f"has been updated successfully."
                )

            else:
                messages.error(
                    request,
                    "Data posted was not valid "
                    "to update a project."
                )

        else:
            messages.error(
                request,
                "Data should be posted when "
                "attempting to update a project."
            )

        return redirect(
            reverse("edit_folio_projects",
                    kwargs={"folio_id": folio_id})
        )

    else:
        messages.error(
            request,
            "You cannot interact with "
            "projects that are not your own."
        )
        return redirect("view_library")


@login_required
def update_projects_attached_to_folio(request, folio_id):
    """
    Updates which projects are attached
    to the currently viewed folio
    """

    if user_is_author_of_folio(request.user, folio_id):

        if request.method == "POST":
            data = json.loads(request.body)
            list_of_projects = data['projects']
            list_of_projects.sort(reverse=False, key=sort_by_id)

            projects = Project.objects.filter(
                id__in=[project['id'] for project in list_of_projects]
            )
            folio = get_object_or_404(Folio, pk=folio_id)

            # Iterate through project in db & status given from user actions
            for project_in_db, project_status in zip(projects,
                                                     list_of_projects):
                # Ensure ID's match
                if project_in_db.id == int(project_status['id']):
                    # Add/remove folio or continue based on is_attached
                    # status & if the folio already exists in project folios
                    if project_status['is_attached']:
                        if project_in_db.folios.filter(pk=folio_id).exists():
                            continue
                        else:
                            project_in_db.folios.add(folio)
                    else:
                        if project_in_db.folios.filter(pk=folio_id).exists():
                            project_in_db.folios.remove(folio)
                        else:
                            continue

                    messages.success(
                        request,
                        f"The projects attached to the {folio.name} "
                        f"folio has been successfully updated."
                    )

                else:
                    print(
                        "DEBUG: Project id's didn't match, "
                        "likely sorting error"
                    )

            return HttpResponse("OK")

        else:
            raise exceptions.BadRequest

    else:
        raise exceptions.PermissionDenied


@login_required
def delete_folio_project(request, project_id, folio_id):
    """
    Deletes a user's folio project
    """

    if user_is_author_of_snippet(request.user, 'project', project_id):

        if request.method == "POST":
            project = get_object_or_404(Project, pk=project_id)
            project.delete()
            messages.success(
                request,
                f"The {project.project_title} project "
                f"has been deleted successfully."
            )

        else:
            messages.error(
                request,
                "A delete command should "
                "be sent as a POST request."
            )

        return redirect(
            reverse("edit_folio_projects",
                    kwargs={"folio_id": folio_id})
        )

    else:
        messages.error(
            request,
            "You cannot delete projects "
            "that are not your own."
        )
        return redirect("view_library")
