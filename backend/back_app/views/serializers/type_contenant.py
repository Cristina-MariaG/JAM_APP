from rest_framework import serializers

from back_app.models import TypeContenant


class TypeContenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeContenant
        fields = ("id", "type_contenant")
