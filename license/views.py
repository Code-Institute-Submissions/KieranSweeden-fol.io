"""
Views for the pages related to the license store
"""

from django.conf import settings
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from account.models import UserAccount

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

    user_details = get_object_or_404(
        UserAccount,
        user=request.user
    )

    if user_details.first_name and user_details.last_name:
        user_details.full_name = (f"{user_details.first_name} "
                                  f"{user_details.last_name}")
    else:
        user_details.full_name = ""

    form = LicensePurchaseForm(initial={
        'purchaser_full_name': user_details.full_name,
        'purchaser_email': request.user.email,
        'purchaser_phone_number': user_details.phone_number,
        'purchaser_street_address1': user_details.default_street_address1,
        'purchaser_street_address2': user_details.default_street_address2,
        'purchaser_town_or_city': user_details.default_town_or_city,
        'purchaser_postcode': user_details.default_postcode,
        'purchaser_county': user_details.default_county,
        'purchaser_country': user_details.default_country
    })

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
                        'purchaser_country'],
                    "save_billing_as_default": request.POST.get(
                        'save_billing_details'),
                },
                mode='payment',
                success_url=(
                    f"{settings.URL}license/success"
                    f"?session_id={{CHECKOUT_SESSION_ID}}"
                ),
                cancel_url=(
                    f"{settings.URL}license/purchase/"
                    f"?failed_payment=True"
                ),
            )

            return redirect(checkout_session.url, status=303)


@login_required
def order_history(request):
    """
    Collects the user's list of folios
    and presents then within the library page
    """

    user_list_of_prev_purchases = LicensePurchase.objects.filter(
        user=request.user.id
    ).order_by(
        '-purchase_date'
    )

    context = {
        "license_purchases": user_list_of_prev_purchases
    }

    return render(request, "license/order_history.html", context=context)


@login_required
def checkout_session_success(request):
    """
    Presents a license purchase success
    page to the user confirming their purchase
    """

    stripe_session_id = request.GET.get('session_id', None)

    if stripe_session_id:
        prev_success_session = stripe.checkout.Session.retrieve(
            stripe_session_id
        )

        if prev_success_session:
            session_pid = prev_success_session['payment_intent']

            prev_success_purchase = get_object_or_404(
                LicensePurchase,
                stripe_pid=session_pid
            )

            context = {
                "license_purchase": prev_success_purchase
            }

            messages.success(
                request,
                "License was successfully purchased"
            )

            return render(
                request,
                "license/purchase_success.html",
                context=context
            )

    else:
        return redirect("view_library")
