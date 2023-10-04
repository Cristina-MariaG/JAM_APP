import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import status

from back_app.models import User

# logger = logging.getLogger("jam")


class UserCollection(APIView):
    # @HandleError.handle_error("User collection get -")
    def post(self, request, *args, **kwargs):
        # logger.debug("Start Collection post user")
        response = dict()

        password = request.data["password"]
        email = request.data["email"]

        user = User.objects.get(email=email)

        status_code = status.HTTP_200_OK
        return Response(user, status=status_code)
