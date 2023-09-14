from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Collection(APIView):
    def get(self, request, *args, **kwargs):
        # logger.debug("Start Collection  get object")
        response = dict()
        response["status"] = "ok"

        return Response(response)
