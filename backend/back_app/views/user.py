import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password

from back_app.models import Role, User
from back_app.views.utilities.handle_errors import (
    HandleError,
)

from django.conf import settings

logger = logging.getLogger("jam")


class UserCollection(APIView):
    @HandleError.handle_error("User collection post -")
    def post(self, request, *args, **kwargs):
        # logger.debug("Start Collection post user")
        response = dict()

        password = request.data["password"]
        email = request.data["email"]

        if not check_password(password, user.password):
            status_code = status.HTTP_401_UNAUTHORIZED
            return Response(status=status_code)

        user = User.objects.get(email=email)

        if user:
            try:
                # payload = jwt_payload_handler(user)

                # # token = jwt.encode(payload, settings.SECRET_KEY)
                # token = jwt_encode_handler(payload, settings.SECRET_KEY)

                user_details = {}

                user_details["email"] = user.email

                user_details["token"] = token

                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e

        else:
            res = {
                "error": "can not authenticate with the given credentials or the account has been deactivated"
            }

            return Response(res, status=status.HTTP_403_FORBIDDEN)

        # status_code = status.HTTP_200_OK

        # return Response(user, status=status_code)


class UserSignInCollection(APIView):
    @HandleError.handle_error("User collection post -")
    def post(self, request, *args, **kwargs):
        # logger.debug("Start Collection post user")

        password = request.data["password"]
        email = request.data["email"]
        hashed = make_password(password, salt=None, hasher="default")

        role = Role.objects.get(role="classical_user")
        logger.error(role.id_role)

        user = User.objects.create(email=email, password=hashed, role=role)

        user = User.objects.get(email=email)
        logger.error("user")
        logger.error(user)
        if user:
            logger.error("bf payload")
            # payload = jwt_payload_handler(user)
            # logger.error(payload)

            # # token = jwt.encode(payload, settings.SECRET_KEY)
            # token = jwt_encode_handler(payload, settings.SECRET_KEY)

            user_details = {}
            logger.error("***")
            logger.error(user.email)
            logger.error(user["email"])
            user_details["email"] = user["email"]

            user_details["token"] = token

            return Response(user_details, status=status.HTTP_200_OK)
        else:
            res = {
                "error": "can not authenticate with the given credentials or the account has been deactivated"
            }

            return Response(res, status=status.HTTP_403_FORBIDDEN)

        # status_code = status.HTTP_200_OK
        # return Response(user, status=status_code)
