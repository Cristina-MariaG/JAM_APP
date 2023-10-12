from rest_framework import serializers
from back_app.models import LineOrder, Order


class LineOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineOrder
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    line_orders = LineOrderSerializer(
        many=True, read_only=True
    )  # Si vous souhaitez inclure les lignes de commande dans la sérialisation

    class Meta:
        model = Order
        fields = "__all__"
