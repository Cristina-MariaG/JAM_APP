import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.models import TypeContenant
from back_app.views.serializers.type_contenant import TypeContenantSerializer

logger = logging.getLogger("jam")


class ContenantTypeCollection(APIView):
    @HandleError.handle_error("Jam ContenantTypeCollection get -")
    def get(self, request, *args, **kwargs):
        response = dict()

        contenant_types = TypeContenant.objects.all()
        serializer = TypeContenantSerializer(contenant_types, many=True)

        response["contenant_types"] = serializer.data

        return Response(response)
