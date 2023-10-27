import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import  Flavor
from back_app.views.serializers.flavor import FlavorSerializer

logger = logging.getLogger("jam")


class FlavorCollection(APIView):
    @HandleError.handle_error("Jam FlavorCollection get -")
    def get(self, request, *args, **kwargs):
        logger.debug("Start FlavorCollection get")
        response = dict()

        data = Flavor.objects.all()
        serializer = FlavorSerializer(data, many=True)

        response["flavours"] = serializer.data

        logger.debug("End FlavorCollection get")
        return Response(response)
