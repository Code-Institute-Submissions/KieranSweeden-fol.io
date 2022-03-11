"""
Views for the pages related to the user's folio library
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def view_library(request):
    """
    View to return the folio home page page
    """
    return render(request, "library/view_library.html")
