"""
The following are views that overwrite
django's error pages and replace's them
with custom fol.io error templates
"""

from django.shortcuts import render


def bad_request_400(request, exception):
    """
    Renders the bad request template
    for 400 errors
    """

    return render(
        request,
        "400.html",
        status=400
    )


def user_forbidden_403(request, exception):
    """
    Renders the user forbidden template
    for 403 errors
    """

    return render(
        request,
        "403.html",
        status=403
    )


def page_not_found_404(request, exception):
    """
    Renders the page not found template
    for 404 errors
    """

    return render(
        request,
        "404.html",
        status=404
    )


def server_error_500(request):
    """
    Renders the page not found template
    for 404 errors
    """

    return render(
        request,
        "500.html",
        status=500
    )
