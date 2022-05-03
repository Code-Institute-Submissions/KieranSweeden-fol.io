"""
The following are views that overwrite
django's error pages and replace's them
with custom fol.io error templates
"""

from django.shortcuts import render


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
