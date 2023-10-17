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
    @HandleError.handle_error("Jam collection get -")
    def get(self, request, *args, **kwargs):
        response = dict()

        brand_list = Brand.objects.all()
        serializer = BrandSerializer(brand_list, many=True)

        response["brand_list"] = serializer.data

        return Response(response)
