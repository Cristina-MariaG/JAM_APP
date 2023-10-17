from back_app.views.serializers.order import LineOrderSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from django.conf import settings
from datetime import datetime
from datetime import datetime
import logging
import stripe
import jwt
from back_app.models import Order

logger = logging.getLogger("jam")

domain_url = "http://localhost:8000/"


class CheckoutCollection(APIView):
    @HandleError.handle_error("Jam collection get -")
    def post(self, request, *args, **kwargs):
        data = request.data
        logger.error(request.data)

        line_items = []

        user_id = decode_token(data["token"])
        if not user_id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        order_id = create_order(request.data, user_id)

        for el in data["cart"]:
            line_items.append(
                {
                    "price_data": {
                        # Convert the price from a string to an integer value in cents for Stripe
                        # (which displays prices in cents) and then cast it to an integer.
                        # This is done to avoid potential errors with Stripe due to non-integer values.
                        "unit_amount": int(float(el["price"]) * 100),
                        "currency": "eur",
                        "product_data": {"name": el["name"]},
                    },
                    "quantity": el["selectedQuantity"],
                }
            )
            create_line_order_for_order_id(order_id, el)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancel-payment",
            payment_method_types=["card"],
            mode="payment",
            line_items=line_items,
        )
        logger.error(checkout_session)
        return Response({"url": checkout_session["url"], "order_id": order_id})


class CheckoutSuccess(APIView):
    @HandleError.handle_error("Jam CheckoutSuccess get -")
    def post(self, request, *args, **kwargs):
        logger.error(request.data)
        order_id = request.data.get("order_id")
        if not order_id or order_id == -1:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.get(id=order_id)
        order.status = "PAYMENT_OK"
        order.save()
        return Response({"status": "ok"})


class CheckoutCancel(APIView):
    @HandleError.handle_error("Jam CheckoutSuccess get -")
    def delete(self, request, *args, **kwargs):
        logger.error(request.data)
        order_id = kwargs.get("id")

        order = Order.objects.get(id=order_id)
        if not order_id or order_id == -1 or not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            order.delete()

        return Response({"status": "ok"})


def create_order(data, user_id):
    order_data = {}
    order_data["date_order"] = datetime.now()
    order_data["user"] = user_id
    order_data["status"] = "PAYMENT_WAITING"
    order_data["total"] = data["total"]

    serializer = OrderSerializer(data=order_data)
    if serializer.is_valid():
        order = serializer.save()
        return order.id


def create_line_order_for_order_id(order_id, product):
    line_order = {}

    line_order["order"] = order_id
    line_order["product"] = product["id"]
    line_order["quantity"] = product["selectedQuantity"]
    line_order["subtotal"] = int(product["selectedQuantity"]) * float(product["price"])

    serializer = LineOrderSerializer(data=line_order)
    if serializer.is_valid():
        serializer.save()
        return serializer.data.get("id")

    return False


def decode_token(token):
    try:
        decoded_access_token = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
            options={"verify_exp": True},
        )
        logger.error(decoded_access_token)

        user_id = decoded_access_token["user_id"]
        logger.error(decoded_access_token)
        # exp_timestamp = decoded_access_token["exp"]

        # current_timestamp = datetime.timestamp(datetime.now())

        if not user_id:
            return False

        return user_id
    except Exception:
        return False
