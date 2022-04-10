"""
Contains the webhook view that
listens for stripe webhooks
"""

from django.conf import settings
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

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
        # Invalid payload
        print(error)
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as error:
        # Invalid signature
        print(error)
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        print(session)

    # Passed signature verification
    return HttpResponse(status=200)
