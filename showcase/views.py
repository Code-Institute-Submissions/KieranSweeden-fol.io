from django.shortcuts import (
    render,
    get_object_or_404
)
from account.models import UserAccount
from suite.models import Folio, Project
from suite.models import Skill
from suite.functions import (
    is_tech_skill,
    is_soft_skill
)


def view_folio_projects(request, folio_id=None):
    """
    View projects within folio
    """
    folio = get_object_or_404(Folio, pk=folio_id)
    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    projects = Project.objects.filter(folios=folio)

    context = {
        "user": request.user,
        "folio": folio,
        "author": author,
        "projects": projects
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
    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    skills = list(Skill.objects.filter(
        author_id=request.user
    ))

    tech_skills = list(filter(is_tech_skill, skills))
    soft_skills = list(filter(is_soft_skill, skills))

    context = {
        "user": request.user,
        "folio": folio,
        "author": author,
        "tech_skills": tech_skills,
        "soft_skills": soft_skills
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
    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    context = {
        "user": request.user,
        "folio": folio,
        "author": author,
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
    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    context = {
        "user": request.user,
        "folio": folio,
        "author": author,
    }

    return render(
        request,
        'showcase/view_folio_contact.html',
        context=context)
