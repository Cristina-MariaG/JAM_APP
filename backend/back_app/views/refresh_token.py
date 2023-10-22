import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from back_app.views.utilities.handle_errors import (
    HandleError,
)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

logger = logging.getLogger("jam")


class RefreshTokenData(APIView):
    @HandleError.handle_error("Jam RefreshToken delete -")
    def post(self, request, *args, **kwargs):
        logger.debug("Start RefreshToken delete ")
        response = dict()

        refresh_token = request.data["refresh_token"]
        if refresh_token:
            refresh = RefreshToken(refresh_token)

            response["token"] = {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_401_UNAUTHORIZED

        logger.debug("End RefreshToken delete")
        return Response(response, status=status_code)
