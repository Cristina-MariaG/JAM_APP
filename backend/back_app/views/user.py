import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password

from back_app.models import Role, User
from back_app.views.utilities.handle_errors import (
    HandleError,
)
from back_app.views.serializers.user import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken



logger = logging.getLogger("jam")


class UserCollection(APIView):
    @HandleError.handle_error("User collection post -")
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        validated_data = user_serializer.validated_data

        try:
            user = User.objects.get(email=validated_data["email"])
        except User.DoesNotExist:
            return Response(
                {"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND
            )

        if not check_password(validated_data["password"], user.password):
            return Response(
                {"error": "Mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        response_data = {
            "token": {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            },
            "user": {"email": user.email, "role": user.role.role},
        }

        return Response(response_data, status=status.HTTP_200_OK)


class UserInscriptionCollection(APIView):
    @HandleError.handle_error("User collection create-")
    def post(self, request, *args, **kwargs):
        logger.debug("Start Collection post user")

        password = request.data["password"]
        email = request.data["email"]

        user = User.objects.filter(email=email)
        if user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        hashed = make_password(password, salt=None, hasher="default")

        role = Role.objects.get(role="classical_user")

        user = User.objects.create(email=email, password=hashed, role=role)

        user = User.objects.get(email=email)

        if user:
            return Response(status=status.HTTP_200_OK)
        else:
            res = {
                "error": "can not authenticate with the given credentials or the account has been deactivated"
            }

            return Response(res, status=status.HTTP_403_FORBIDDEN)
