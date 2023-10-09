import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Product
from back_app.views.serializers.product import ProductSerializer, ProductsSerializer

logger = logging.getLogger("jam")


class ProductsCollection(APIView):
    @HandleError.handle_error("Jam collection get -")
    def get(self, request, *args, **kwargs):
        response = dict()

        # with the newt 2 lines we can get all the informations for all the products
        # products = Product.objects.prefetch_related(
        #     "productingredient_set__ingredient"
        # ).all()
        # serializer = ProductsSerializer(products, many=True)

        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)

        response["products"] = serializer.data

        return Response(response)


class ProductDetailsCollection(APIView):
    @HandleError.handle_error("Jam collection get -")
    def get(self, request, *args, **kwargs):
        response = dict()
        product_id = kwargs.get("id")

        product = Product.objects.prefetch_related(
            "productingredient_set__ingredient"
        ).get(id=product_id)

        serializer = ProductSerializer(product)

        response["product_id"] = serializer.data
        return Response(response)
