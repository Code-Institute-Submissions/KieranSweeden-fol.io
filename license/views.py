"""
Views for the pages related to the license store
"""

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import stripe

from .models import LicensePurchase
from .forms import LicensePurchaseForm

stripe.api_key = settings.STRIPE_PRIVATE_KEY


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
@csrf_exempt
def create_checkout_session(request):
    """
    Creates a stripe checkout session
    """

    if request.method == "POST":
        form = LicensePurchaseForm(request.POST)
        if form.is_valid():

            # Create stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                customer_email=form.cleaned_data[
                        'purchaser_email'
                ],
                line_items=[
                    {
                        'price': settings.FOLIO_LICENSE_PRICE_ID,
                        'adjustable_quantity': {
                            'enabled': True,
                            'minimum': 1,
                            'maximum': 50,
                        },
                        'quantity': form.cleaned_data[
                            'no_of_licenses_purchased'
                        ]
                    },
                ],
                metadata={
                    "user_id": request.user.id,
                    "purchaser_full_name": form.cleaned_data[
                        'purchaser_full_name'],
                    "purchaser_phone_number": form.cleaned_data[
                        'purchaser_phone_number'],
                    "purchaser_street_address1": form.cleaned_data[
                        'purchaser_street_address1'],
                    "purchaser_street_address2": form.cleaned_data[
                        'purchaser_street_address2'],
                    "purchaser_town_or_city": form.cleaned_data[
                        'purchaser_town_or_city'],
                    "purchaser_postcode": form.cleaned_data[
                        'purchaser_postcode'],
                    "purchaser_county": form.cleaned_data[
                        'purchaser_county'],
                    "purchaser_country": form.cleaned_data[
                        'purchaser_country']
                },
                mode='payment',
                success_url=f'{settings.URL}library/',
                cancel_url=f'{settings.URL}license/purchase/',
            )

            return redirect(checkout_session.url, status=303)


@login_required
def order_history(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    return render(request, "license/order_history.html")
