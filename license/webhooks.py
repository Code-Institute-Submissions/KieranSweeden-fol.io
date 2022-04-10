"""
Contains the webhook view that
listens for stripe webhooks
"""

from django.conf import settings
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .webhook_handler import StripeWebHookHandlers

import stripe

stripe.api_key = settings.STRIPE_PRIVATE_KEY
endpoint_secret = settings.STRIPE_ENDPOINT_SECRET


@require_POST
@csrf_exempt
def stripe_webhook(request):
    """
    Listens for stripe webhooks
    """

    # Grab payload
    payload = request.body.decode('utf-8')
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as error:
        return HttpResponse(
            status=400,
            content=(
                f'Webhook received but payload provided was invalid | '
                f'ERROR: {error}'
            )
        )

    except stripe.error.SignatureVerificationError as error:
        return HttpResponse(
            status=400,
            content=(
                f'Webhook received but header signature was invalid | '
                f'ERROR: {error}'
            )
        )
    except Exception as error:
        return HttpResponse(
            status=400,
            content=(
                f"Webhook was received but it's invalid | "
                f'ERROR: {error}'
            )
        )

    stripe_event_map = {
        'checkout.session.completed':
        StripeWebHookHandlers.handle_checkout_session_completed,
        'payment_intent.payment_failed':
        StripeWebHookHandlers.handle_payment_intent_failed
    }

    stripe_event_handler = stripe_event_map.get(
        event['type'],
        StripeWebHookHandlers.handle_event
    )

    return stripe_event_handler(request, event)
