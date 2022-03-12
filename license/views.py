"""
Views for the pages related to the license store
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def purchase_license(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "license/purchase_license.html")


@login_required
def order_history(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "license/order_history.html")
