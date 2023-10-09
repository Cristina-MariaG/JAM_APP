from rest_framework import serializers
from back_app.models import ProductIngredient
from back_app.views.serializers.ingredient import IngredientSerializer


class ProductIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = ProductIngredient
        fields = ("id", "ingredient", "quantity", "product")
