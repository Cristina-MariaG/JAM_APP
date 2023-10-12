import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Category
from back_app.views.serializers.category import CategorySerializer

logger = logging.getLogger("jam")


class FilterCollection(APIView):
    @HandleError.handle_error("Jam collection get -")
    def get(self, request, *args, **kwargs):
        response = dict()
        logger.error(request)
        params = request.GET.dict()
        param1 = request.GET.getlist("categories[]", None)
        param2 = request.GET.get("minPriceUse", None)
        param3 = request.GET.get("maxPriceUser", None)
        logger.error(params)
        logger.error(param1)
        logger.error(param2)
        logger.error(param3)

        # categories = Category.objects.all()
        # serializer = CategorySerializer(categories, many=True)

        # response["categories"] = serializer.data

        return Response(response)
