"""
Views for the pages related to the user's folio library
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def view_library(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "library/view_library.html")


@login_required
def create_folio(request):
    """
    Creates a brand new folio when called
    """
