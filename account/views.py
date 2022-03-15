"""
Views for the pages related to the user's account
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserAccount
from .forms import AccountDetailsForm

# Create your views here.


@login_required
def account_details(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    profile = get_object_or_404(UserAccount, user=request.user)

    form = AccountDetailsForm(instance=profile)

    template = "account/account_details.html"

    context = {
        "form": form
    }

    return render(request, template, context)


@login_required
def billing_details(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "account/billing_details.html")
