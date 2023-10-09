from rest_framework import serializers

from back_app.models import Product
from back_app.views.serializers.product_ingredient import ProductIngredientSerializer


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "image",
            "price",
            "flavor",
            "type_contenant",
            "category",
        )


class ProductSerializer(serializers.ModelSerializer):
    ingredients = ProductIngredientSerializer(source="productingredient_set", many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "image",
            "price",
            "flavor",
            "type_contenant",
            "brand",
            "promotion",
            "stock_disponible",
            "category",
            "quantity",
            "ingredients",
        )
