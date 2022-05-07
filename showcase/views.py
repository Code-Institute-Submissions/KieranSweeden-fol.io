from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import UserAccount
from suite.models import Folio, Project
from suite.models import Skill, Profile
from suite.functions import (
    is_tech_skill,
    is_soft_skill
)
from .forms import SendAuthorMessageForm


def view_folio_projects(request, folio_id=None):
    """
    View projects within folio
    """

    folio = get_object_or_404(Folio, pk=folio_id)

    if not folio.is_published and folio.author_id != request.user:

        return render(
            request,
            'showcase/folio_is_not_published.html'
        )

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

    if not folio.is_published and folio.author_id != request.user:

        return render(
            request,
            'showcase/folio_is_not_published.html'
        )

    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    skills = list(Skill.objects.filter(folios=folio))

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

    if not folio.is_published and folio.author_id != request.user:

        return render(
            request,
            'showcase/folio_is_not_published.html'
        )

    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    profiles = list(Profile.objects.filter(folios=folio))

    context = {
        "user": request.user,
        "folio": folio,
        "author": author,
        "profiles": profiles
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

    if not folio.is_published and folio.author_id != request.user:

        return render(
            request,
            'showcase/folio_is_not_published.html'
        )

    author = get_object_or_404(
        UserAccount,
        pk=folio.author_id.id
    )

    author_user_account = get_object_or_404(
        User,
        pk=folio.author_id.id
    )

    message_form = SendAuthorMessageForm()

    context = {
        "user": author_user_account,
        "folio": folio,
        "author": author,
        "form": message_form
    }

    return render(
        request,
        'showcase/view_folio_contact.html',
        context=context)


def message_author(request, author_email, folio_id=None):
    """
    Functionality that sends a message
    to the author of the viewed folio.
    """

    if request.method == "POST":
        form = SendAuthorMessageForm(request.POST)

        if form.is_valid():
            send_mail(
                f"fol.io Direct Message: {form.cleaned_data['subject']}",
                form.cleaned_data['message'],
                form.cleaned_data['sender_email'],
                [author_email]
            )

            messages.success(
                request,
                "Your message has been sent."
            )

            return redirect(
                'view_folio_contact',
                folio_id=folio_id
            )
