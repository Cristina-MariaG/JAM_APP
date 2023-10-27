import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Ingredient
from back_app.views.serializers.ingredient import IngredientSerializer

logger = logging.getLogger("jam")


class IngredientCollection(APIView):
    @HandleError.handle_error("Jam FlavorCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start FlavorCollection get")
        response = dict()

        data = Ingredient.objects.all()
        serializer = IngredientSerializer(data, many=True)

        response["ingredients"] = serializer.data

        logger.debug("End FlavorCollection get")
        return Response(response)
