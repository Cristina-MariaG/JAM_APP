from rest_framework import serializers

from back_app.models import StockDisponible


class StockDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDisponible
        fields = ("id", "stock_disponible")
