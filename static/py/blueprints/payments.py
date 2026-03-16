import json
import os

import braintree
import stripe
from flask import render_template, Blueprint, request, jsonify, send_file, redirect

from static.py.api import webpage, products, accounts, passwords, carts, orders
from static.py.api.others import session

blueprint = Blueprint("payment_route", __name__, url_prefix="/payments")

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.getenv("BRAINTREE_MERCHANT_ID"),
        public_key=os.getenv("BRAINTREE_PUBLIC_KEY"),
        private_key=os.getenv("BRAINTREE_PRIVATE_KEY")
    )
)

@blueprint.route("/stripe/checkout", methods=["GET", "POST"])
def stripe_checkout():
    data = request.json
    stripe_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': data['item_name']},
                'unit_amount': data['amount_cents']
            },
            'quantity': 1
        }],
        mode='payment',
        success_url='/success',
        cancel_url='/cancel'
    )
    return jsonify({'id': stripe_session.id})
