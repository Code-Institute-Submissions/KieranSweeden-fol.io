"""
Views for the pages related to the license store
"""

from django.conf import settings
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import LicensePurchase
from .forms import LicensePurchaseForm

import stripe


@login_required
def purchase_license(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """
    # Create a fresh instance of the license purchase form
    form = LicensePurchaseForm()

    context = {
        "form": form
    }

    return render(request,
                  "license/purchase_license.html",
                  context=context)


@login_required
def create_checkout_session(request):
    """
    Creates a stripe checkout session
    """

    if request.method == "POST":
        form = LicensePurchaseForm(request.POST)
        if form.is_valid():
            # Set stripe api key
            stripe.api_key = settings.STRIPE_PRIVATE_KEY

            # Create stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                customer_email=form.cleaned_data[
                        'purchaser_email'
                ],
                line_items=[
                    {
                        'price': settings.FOLIO_LICENSE_PRICE_ID,
                        'quantity': form.cleaned_data[
                            'no_of_licenses_purchased'
                        ]
                    },
                ],
                mode='payment',
                success_url=f'{settings.URL}/library/',
                cancel_url=f'{settings.URL}/license/purchase/',
            )

            return redirect(checkout_session.url, status=303)


@login_required
def order_history(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "license/order_history.html")
