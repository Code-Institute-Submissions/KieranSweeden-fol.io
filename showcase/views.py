from django.shortcuts import render, get_object_or_404
from suite.models import Folio


def view_folio_projects(request, folio_id=None):
    """
    View projects within folio
    """

    folio = get_object_or_404(Folio, pk=folio_id)

    context = {
        "folio": folio,
        "user": request.user
    }

    return render(
        request,
        'showcase/view_folio_projects.html',
        context=context)


def view_folio_skills(request, folio_id=None):
    """
    View skills within folio
    """

    folio = get_object_or_404(Folio, pk=folio_id)

    context = {
        "folio": folio
    }

    return render(
        request,
        'showcase/view_folio_skills.html',
        context=context)


def view_folio_profile(request, folio_id=None):
    """
    View profile page within folio
    """

    folio = get_object_or_404(Folio, pk=folio_id)

    context = {
        "folio": folio
    }

    return render(
        request,
        'showcase/view_folio_profile.html',
        context=context)


def view_folio_contact(request, folio_id=None):
    """
    View contact page within folio
    """

    folio = get_object_or_404(Folio, pk=folio_id)

    context = {
        "folio": folio
    }

    return render(
        request,
        'showcase/view_folio_contact.html',
        context=context)
