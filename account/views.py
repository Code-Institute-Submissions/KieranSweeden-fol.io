"""
Views for the pages related to the user's account
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def account_details(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """



    return render(request, "account/account_details.html")


@login_required
def billing_details(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "account/billing_details.html")
