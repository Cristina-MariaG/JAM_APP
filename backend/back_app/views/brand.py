import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import Brand
from back_app.views.serializers.brand import BrandSerializer

logger = logging.getLogger("jam")


class BrandCollection(APIView):
    @HandleError.handle_error("Jam BrandCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start BrandCollection get")
        response = dict()

        brand_list = Brand.objects.all()
        serializer = BrandSerializer(brand_list, many=True)

        response["brand_list"] = serializer.data

        logger.debug("End BrandCollection get")
        return Response(response)
