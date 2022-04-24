"""
Views for the pages related to the user's account
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserAccount
from .forms import AccountDetailsForm, BillingDetailsForm


@login_required
def account_details(request):
    """
    The view that presents and allows the
    user to update their account details.
    """

    profile = get_object_or_404(UserAccount, user=request.user)

    if request.method == "POST":
        form = AccountDetailsForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your account details have been updated successfully"
            )

    else:
        form = AccountDetailsForm(instance=profile)

    template = "account/account_details.html"
    context = {
        "form": form
    }
    return render(request, template, context)


@login_required
def billing_details(request):
    """
    The view that presents and allows the
    user to update their billing details.
    """

    profile = get_object_or_404(UserAccount, user=request.user)

    if request.method == "POST":
        form = BillingDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your billing details have been updated successfully"
            )

    else:
        form = BillingDetailsForm(instance=profile)

    template = "account/billing_details.html"
    context = {
        "form": form
    }
    return render(request, template, context)
