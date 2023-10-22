import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Category
from back_app.views.serializers.category import CategorySerializer

logger = logging.getLogger("jam")


class CategoryCollection(APIView):
    @HandleError.handle_error("Jam CategoryCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start CategoryCollection get")
        response = dict()

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        response["categories"] = serializer.data

        logger.debug("End CategoryCollection get")
        return Response(response)
