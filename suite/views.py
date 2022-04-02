"""
Views for the pages related to the folio suite
"""

from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib.auth.decorators import login_required
from suite.models import Folio, Project
from suite.functions import id_has_been_provided, user_is_author_of_folio, sortByID
from suite.forms import FolioProjectForm
import json


@login_required
def open_suite(request, folio_id=None):
    """
    This view attempts to direct the user to
    the suite. If a folio id has not been provided,
    the user will be directed to the select folio view.
    Else they'll be directed to the suite viewing folio.
    """

    # Assess whether folio_id has been provided
    if id_has_been_provided(folio_id):
        # If it has, direct the user to folio view
        # attaching the folio id as an argument
        # return redirect('view_folio_projects', folio_id=folio_id)

        # Create response object to redirect user
        response = redirect(reverse("edit_folio_projects",
                            kwargs={"folio_id": folio_id}))

        # Store folio_id in cookies
        response.set_cookie("latest_folio", folio_id)

        return response

    # With no folio_if provided, check the user's latest folio cookie
    elif request.COOKIES.get('latest_folio') is not None:

        # Grab the folio_id given the cookie exists
        folio_id = request.COOKIES.get('latest_folio')

        # Check the user is actually the author of the folio
        if user_is_author_of_folio(request.user, folio_id):

            # Open folio if true
            return redirect(reverse("edit_folio_projects",
                                    kwargs={"folio_id": folio_id}))

    # If folio_id checks are all false, direct user to select folio page
    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def select_folio(request):
    """
    If a folio has not been selected when
    entering the suite, this view will prompt
    the user to select a folio from their library,
    """

    if request.method == "POST":

        # Get the id from request
        folio_id = request.POST.get('folio_selected')

        # Create response object to redirect user
        response = redirect(reverse("edit_folio_projects",
                            kwargs={"folio_id": folio_id}))

        # Store folio_id in cookies
        response.set_cookie("latest_folio", folio_id)

        return response

    else:

        # Check the user's cookies for latest folio
        if request.COOKIES.get('latest_folio') is not None:

            # Grab the folio_id given the cookie exists
            folio_id = request.COOKIES.get('latest_folio')

            # Check the user is actually the author of the folio
            if user_is_author_of_folio(request.user, folio_id):

                # Open folio if true
                return redirect(reverse("edit_folio_projects",
                                        kwargs={"folio_id": folio_id}))

        else:

            # Get the users folios
            folios = Folio.objects.filter(
                author_id=request.user
            )

            context = {
                "folios": folios
            }

            return render(request, "suite/select_folio.html", context=context)


@login_required
def edit_folio_projects(request, folio_id=None):
    """
    Presents the projects tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        # Get the specific folio using the id provided
        folio = get_object_or_404(Folio, pk=folio_id)

        # Get the user's projects
        projects = list(Project.objects.filter(
            author_id=request.user
        ))

        # For each project, attach a form to the object
        # And assess whether project is attached to form
        for project in projects:
            project.form = FolioProjectForm(instance=project)

            for attached_folio in project.folios.all():
                project.is_attached_to_current_folio = (
                    attached_folio.id == folio_id
                )

        # Create an empty project form instance
        form = FolioProjectForm()

        # Create context
        context = {
            "folio": folio,
            "projects": projects,
            "form": form
        }

        return render(request, "suite/edit_projects.html", context=context)

    else:

        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def create_folio_project(request, folio_id):
    """
    Creates a new folio project
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        form = FolioProjectForm(request.POST)

        # If form is valid
        if form.is_valid():

            # Partially save the form, as author_id
            # will need to be provided
            project = form.save(commit=False)

            # Save current user as author of project
            project.author_id = request.user

            # Fully save project
            project.save()

            # Return to folio project page using folio id
            return redirect(reverse("edit_folio_projects",
                                    kwargs={"folio_id": folio_id}))


@login_required
def update_folio_project(request, project_id, folio_id):
    """
    Updates an existing folio project
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get current project
        project_in_db = get_object_or_404(Project, pk=project_id)

        form = FolioProjectForm(request.POST, instance=project_in_db)

        if form.is_valid():

            form.save()

        # Return to folio project page using folio id
        return redirect(reverse("edit_folio_projects",
                                kwargs={"folio_id": folio_id}))


@login_required
def update_projects_attached_to_folio(request, folio_id):
    """
    Updates which projects are attached
    to the currently viewed folio
    """

    if request.method == "POST":
        # Retrieve list of project status's sorted by id
        data = json.loads(request.body)
        list_of_projects = data['projects']
        list_of_projects.sort(reverse=False, key=sortByID)

        # Grab users projects from DB using ID's provided
        projects = Project.objects.filter(
             id__in=[project['id'] for project in list_of_projects]
        )

        # Get currently viewed folio
        folio = get_object_or_404(Folio, pk=folio_id)

        # Iterate through project in db & status given from user actions
        for project_in_db, project_status in zip(projects, list_of_projects):
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

        # Return an OK response
        return HttpResponse("OK")


@login_required
def delete_folio_project(request, project_id, folio_id):
    """
    Deletes a user's folio project
    """

    # Ensure the request made is a POST request
    if request.method == "POST":

        # Get the project
        project_in_db = get_object_or_404(Project, pk=project_id)

        # Delete the project from the database
        project_in_db.delete()

        # Return to folio project page using folio id
        return redirect(reverse("edit_folio_projects",
                                kwargs={"folio_id": folio_id}))


@login_required
def edit_folio_skills(request, folio_id=None):
    """
    Presents the skills tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_skills.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def edit_folio_profile(request, folio_id=None):
    """
    Presents the profile tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_profile.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")


@login_required
def edit_folio_contact(request, folio_id=None):
    """
    Presents the contact tab of the
    folio to the user.
    """

    if id_has_been_provided(folio_id):

        folio = get_object_or_404(Folio, pk=folio_id)

        context = {
            "folio": folio
        }

        return render(request, "suite/edit_contact.html", context=context)

    else:
        # If one hasn't been provided
        return redirect("select_folio")
