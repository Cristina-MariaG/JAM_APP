from rest_framework import serializers

from back_app.models import Product
from back_app.views.serializers.product_ingredient import ProductIngredientSerializer
from back_app.views.serializers.brand import BrandSerializer
from back_app.views.serializers.category import CategorySerializer
from back_app.views.serializers.flavor import FlavorSerializer
from back_app.views.serializers.stock_disponible import (
    StockDisponibleSerializer,
)
from back_app.views.serializers.type_contenant import TypeContenantSerializer


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
    flavor = FlavorSerializer()
    type_contenant = TypeContenantSerializer()
    brand = BrandSerializer()
    stock_disponible = StockDisponibleSerializer()
    category = CategorySerializer()
    ingredients = ProductIngredientSerializer(source="productingredient_set", many=True)

    class Meta:
        model = Product
        fields = "__all__"

