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
from back_app.views.serializers.user import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

logger = logging.getLogger("jam")


class UserCollection(APIView):
    @HandleError.handle_error("User collection post -")
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND
            )

        if not check_password(password, user.password):
            return Response(
                {"error": "Mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        logger.error(user_serializer.data)

        response_data = {
            "token": str(refresh.access_token),
            "user": {"email": user_serializer.data["email"]},
        }

        return Response(response_data, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     password = request.data["password"]
    #     email = request.data["email"]
    #     user = User.objects.get(email=email)

    #     if not check_password(password, user.password):
    #         status_code = status.HTTP_401_UNAUTHORIZED
    #         return Response(status=status_code)

    #     if user:
    #         try:
    #             refresh = RefreshToken.for_user(user)
    #             user_details = {}
    #             user_details["token"] = str(refresh.access_token)
    #             user_details["user"] = {"email": user.email}

    #             return Response(user_details, status=status.HTTP_200_OK)

    #         except Exception as e:
    #             raise e

    #     else:
    #         res = {
    #             "error": "can not authenticate with the given credentials or the account has been deactivated"
    #         }

    #  return Response(res, status=status.HTTP_403_FORBIDDEN)


class UserSignupCollection(APIView):
    @HandleError.handle_error("User collection post -")
    def post(self, request, *args, **kwargs):
        logger.debug("Start Collection post user")

        password = request.data["password"]
        email = request.data["email"]
        hashed = make_password(password, salt=None, hasher="default")

        role = Role.objects.get(role="classical_user")
        logger.error(role.id)

        user = User.objects.create(email=email, password=hashed, role=role)

        user = User.objects.get(email=email)
        logger.error("user")
        logger.error(user)
        if user:
            refresh = RefreshToken.for_user(user)

            user_details = {}
            user_details["token"] = str(refresh.access_token)
            user_details["user"] = {"email": user.email}

            return Response(user_details, status=status.HTTP_200_OK)
        else:
            res = {
                "error": "can not authenticate with the given credentials or the account has been deactivated"
            }

            return Response(res, status=status.HTTP_403_FORBIDDEN)
