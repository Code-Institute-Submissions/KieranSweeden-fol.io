"""
View for the home page of folio
"""

from django.shortcuts import render

import os


# Create your views here.
def index(request):
    """
    View to return the folio home page page
    """

    return render(request, "home/index.html")
