from rest_framework import status

from rest_framework.serializers import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

logger = logging.getLogger("jam")


class HandleError(APIView):
    def handle_error(text):
        def decorator(function):
            def wrapper(*args, **kwargs):
                try:
                    return function(*args, **kwargs)

                except TokenError as e:
                    if (
                        isinstance(e, TokenError)
                        and str(e) == "Token is invalid or expired"
                    ):
                        return Response(
                            {"error": "Token invalide ou expiré"},
                            status=status.HTTP_401_UNAUTHORIZED,
                        )
                    else:
                        logger.error(e)
                        return Response(
                            {"error": "Erreur de token inconnue"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                except ObjectDoesNotExist as e:
                    logger.error(f"{text}: Except ObjectDoesNotExist : {str(e)}")
                    return Response(
                        {"status": "ObjectDoesNotExist"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                except ValidationError as e:
                    statusCode = status.HTTP_400_BAD_REQUEST

                    logger.error(
                        f"{text}: Except ValidationError : {str(e)}. {statusCode}"
                    )
                    return Response(status=statusCode)

                except DatabaseError as e:
                    logger.error(f"{text}: Except DatabaseError : {str(e)}")

                    return Response(
                        {"status": "DatabaseError"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except Exception as e:
                    logger.error(f"{text}: Except Exception unknown error : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

            return wrapper

        return decorator
