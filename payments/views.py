import stripe
from django.conf import settings
from django.shortcuts import render,  get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def welcome(request):
    return render(request, "payments/welcome.html")


@csrf_exempt
def create_checkout_session(request):
    YOUR_DOMAIN = "http://10.10.20.61:8000"  # Replace with your domain in production
    
    # Create Stripe checkout session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Product or Service Name',  # Customize your product name here
                },
                'unit_amount': 500,  # Amount in cents (e.g., $5.00)
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/payment/success/',
        cancel_url=YOUR_DOMAIN + '/payment/cancel/',
    )
    
    # Create payment record in DB
    payment = Payment.objects.create(stripe_payment_id=session.id, amount=5.00)
    
    return redirect(session.url, code=303)  # Redirect the user to Stripe's hosted payment page


def success(request):
    return render(request, "payments/success.html")

@csrf_exempt
def cancel(request):
    return render(request, "payments/cancel.html")

def refund_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)

    stripe.Refund.create(
    payment_intent='pi_realPaymentIntentIdHere',
    amount=500,
)

    return render(request, "payments/refund_done.html", {"payment": payment})