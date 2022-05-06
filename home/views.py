"""
View for the home page of folio
"""

from django.shortcuts import render


def index(request):
    """
    View to return the folio home page page
    """

    context = {
        "user": request.user
    }

    return render(
        request,
        "home/index.html",
        context=context
    )
