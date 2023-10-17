import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Product

from django.db.models import Max, Min

logger = logging.getLogger("jam")


class PriceCollection(APIView):
    @HandleError.handle_error("Jam collection get -")
    def get(self, request, *args, **kwargs):
        response = dict()
        price_range = Product.objects.aggregate(Min("price"), Max("price"))

        logger.error(price_range)
        return Response(price_range)
