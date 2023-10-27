import logging
from math import ceil
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import (
    Brand,
    Category,
    Flavor,
    Ingredient,
    Product,
    ProductIngredient,
    StockDisponible,
    TypeContenant,
)
from back_app.views.serializers.product import ProductSerializer, ProductsSerializer
from back_app.views.checkout import verify_validity_decode_token
from django.conf import settings
logger = logging.getLogger("jam")

products_per_page =settings.PRODUCTS_PER_PAGE


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

    @HandleError.handle_error("ProductsCollection collection post -")
    def post(self, request, *args, **kwargs):
        logger.debug("Start ProductsCollection post")
        response = dict()
        logger.error(request.data)
        data = request.data


        user_id = verify_validity_decode_token(data["accessToken"])

        if not user_id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


        category_id = data["categoryId"]
        brand_id = data["brandId"]
        available_stock = data["availableStock"]
        contenant_type_id = data["contenantTypeId"]
        flavor_id = data["flavorId"]
        name = data["name"]
        description = data["description"]
        image = data["image"]
        price = data["price"]
        quantity = data["quantity"]
        promotion = data["promotion"]

        category = Category.objects.get(id=category_id)
        brand = Brand.objects.get(id=brand_id)
        contenant_type = TypeContenant.objects.get(id=contenant_type_id)
        flavor = Flavor.objects.get(id=flavor_id)
        if available_stock == True:
            available_stock = "true"
        else:
            available_stock = "false"

        stock_disponible = StockDisponible.objects.get(stock_disponible=available_stock)

        product = Product.objects.create(
            category=category,
            brand=brand,
            stock_disponible=stock_disponible,
            type_contenant=contenant_type,
            flavor=flavor,
            name=name,
            description=description,
            image=image,
            price=price,
            quantity=quantity,
            promotion=promotion,
        )

        for ingredient_data in data["ingredients"]:
            ingredient_id = ingredient_data["ingredientId"]
            quantity = ingredient_data.get("quantity", None)

            ingredient = Ingredient.objects.get(id=ingredient_id)

            ProductIngredient.objects.create(
                product=product, ingredient=ingredient, quantity=quantity
            )

        logger.debug("End ProductsCollection post")
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
