import logging
from math import ceil
from rest_framework.views import APIView
from rest_framework.response import Response

from stripe import Product
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from django.db.models import Q

from back_app.models import Product, StockDisponible

from back_app.views.serializers.product import ProductsSerializer
from django.conf import settings

logger = logging.getLogger("jam")

products_per_page = settings.PRODUCTS_PER_PAGE


class FilterCollection(APIView):
    @HandleError.handle_error("Jam FilterCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start FilterCollection get ")

        response = dict()
        min_price = request.GET.get("minPriceUser", None)
        max_price = request.GET.get("maxPriceUser", None)
        searched_text = request.GET.get("searchedText", None)
        available_stock_value = request.GET.get("availableStock", None)
        ordonate_by_price = request.GET.get("ordonateByPrice", None)

        categories_selected = request.GET.getlist("categories[]", [])
        contenant_types_selected = request.GET.getlist("typeContenant[]", [])
        brand_list_selected = request.GET.getlist("brandList[]", [])

        contenant_types_selected = list(map(int, contenant_types_selected))
        brand_list_selected = list(map(int, brand_list_selected))
        categories_selected = list(map(int, categories_selected))

        available_stock_id = None
        if available_stock_value:
            available_stock = StockDisponible.objects.get(
                stock_disponible=available_stock_value
            )
            if available_stock:
                available_stock_id = available_stock.id

        if ordonate_by_price:
            order_by = "price"
            if ordonate_by_price == "Descending":
                order_by = "-price"

            filtered_products = Product.objects.filter(
                Q(name__icontains=searched_text) if searched_text else Q(),
                Q(stock_disponible=available_stock_id) if available_stock_id else Q(),
                Q(price__gte=min_price) if min_price is not None else Q(),
                Q(price__lte=max_price) if max_price is not None else Q(),
                Q(category__in=categories_selected)
                if len(categories_selected) != 0
                else Q(),
                Q(type_contenant__in=contenant_types_selected)
                if len(contenant_types_selected) != 0
                else Q(),
                Q(brand__in=brand_list_selected)
                if len(brand_list_selected) != 0
                else Q(),
            ).order_by(order_by)
        else:
            filtered_products = Product.objects.filter(
                Q(name__icontains=searched_text) if searched_text else Q(),
                Q(stock_disponible=available_stock_id) if available_stock_id else Q(),
                Q(price__gte=min_price) if min_price is not None else Q(),
                Q(price__lte=max_price) if max_price is not None else Q(),
                Q(category__in=categories_selected)
                if len(categories_selected) != 0
                else Q(),
                Q(type_contenant__in=contenant_types_selected)
                if len(contenant_types_selected) != 0
                else Q(),
                Q(brand__in=brand_list_selected)
                if len(brand_list_selected) != 0
                else Q(),
            )

        page = int(request.GET.get("page", 0))
        begin_products = page * products_per_page
        end_products = begin_products + products_per_page

        total_products = len(filtered_products)
        total_pages = ceil(total_products / products_per_page)

        if end_products > total_products:
            end_products = total_products

        filtered_products = filtered_products[begin_products:end_products]

        serializer = ProductsSerializer(filtered_products, many=True)
        response["products"] = serializer.data
        response["pages_number"] = total_pages

        logger.debug("End FilterCollection get ")
        return Response(response)
