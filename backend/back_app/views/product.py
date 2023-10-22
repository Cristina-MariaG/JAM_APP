import logging
from math import ceil
from rest_framework.views import APIView
from rest_framework.response import Response

from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Product
from back_app.views.serializers.product import ProductSerializer, ProductsSerializer

logger = logging.getLogger("jam")

products_per_page = 15


class ProductsCollection(APIView):
    @HandleError.handle_error("Jam ProductsCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start get ProductsCollection")
        response = dict()

        # with the newt 2 lines we can get all the informations for all the products
        # products = Product.objects.prefetch_related(
        #     "productingredient_set__ingredient"
        # ).all()
        # serializer = ProductsSerializer(products, many=True)

        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)

        page = int(request.GET.get("page", 0))
        begin_products = page * products_per_page
        end_products = begin_products + products_per_page

        total_products = len(products)
        total_pages = ceil(total_products / products_per_page)

        if end_products > total_products:
            end_products = total_products

        products = products[begin_products:end_products]

        serializer = ProductsSerializer(products, many=True)
        response["products"] = serializer.data
        response["pages_number"] = total_pages

        logger.debug("End ProductsCollection get")
        return Response(response)


class ProductDetailsCollection(APIView):
    @HandleError.handle_error("Jam ProductDetailsCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start ProductDetailsCollection get")
        response = dict()
        product_id = kwargs.get("id")

        product = (
            Product.objects.select_related(
                "flavor", "type_contenant", "brand", "stock_disponible", "category"
            )
            .prefetch_related("ingredients")
            .get(pk=product_id)
        )

        serialized_product = ProductSerializer(product)

        response["product"] = serialized_product.data

        logger.debug("End ProductDetailsCollection get")
        return Response(response)
