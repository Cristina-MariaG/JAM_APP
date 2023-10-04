from rest_framework import status
from arango import (
    ArangoError,
    DocumentDeleteError,
    DocumentGetError,
    DocumentInsertError,
)
from rest_framework.request import Request

from rest_framework.serializers import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings


logger = logging.getLogger("eco_db")

# URL_NOT_REQUIRING_AUTH = settings.URL_NOT_REQUIRING_AUTH


class HandleError(APIView):
    # @staticmethod
    def handle_error(text):
        def decorator(function):
            def wrapper(*args, **kwargs):
                try:
        
                    return function(*args, **kwargs)
                
                except DocumentInsertError as e:
                    recuperateUserIdAndLogError(args)

                    logger.error(f"{text}: Except DocumentInsertError : {str(e)}")

                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except DocumentGetError as e:
                    recuperateUserIdAndLogError(args)

                    logger.error(f"{text}: Except DocumentGetError : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except DocumentDeleteError as e:
                    recuperateUserIdAndLogError(args)

                    logger.error(f"{text}: Except DocumentDeleteError : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                except ObjectDoesNotExist as e:
                    recuperateUserIdAndLogError(args)

                    logger.error(f"{text}: Except ObjectDoesNotExist : {str(e)}")
                    return Response(
                        {"status": "ObjectDoesNotExist"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                except ValidationError as e:
                    recuperateUserIdAndLogError(args)

                    response = responseByErrorSerializerType(e)
                    statusCode = status.HTTP_400_BAD_REQUEST
                    if response["code"][0] == "CODE5":
                        statusCode = status.HTTP_403_FORBIDDEN
                    if response["code"][0] == "CODE6":
                        statusCode = status.HTTP_404_NOT_FOUND

                    logger.error(
                        f"{text}: Except ValidationError : {str(e)}. {response}"
                    )
                    return Response(response, status=statusCode)

                except DatabaseError as e:
                    recuperateUserIdAndLogError(args)
                    logger.error(f"{text}: Except DatabaseError : {str(e)}")

                    return Response(
                        {"status": "DatabaseError"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except ArangoError as e:
                    recuperateUserIdAndLogError(args)

                    logger.error(f"{text}: Except ArangoError : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except Exception as e:
                    recuperateUserIdAndLogError(args)

                    logger.error(f"{text}: Except Exception unknown error : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

            return wrapper

        return decorator


def recuperateUserIdAndLogError(args):
    id_user = None
    for arg in args:
        if isinstance(arg, Request):
            request = arg
            user_value = request.session.get("user", None)
            if user_value:
                id_user = request.session["user"]["id"]
    #   if not request.path.startswith(URL_NOT_REQUIRING_AUTH):

    if id_user:
        logger.error(f"Except Exception user with id: {str(id_user)}")


def responseByErrorSerializerType(e):
    if isinstance(e.get_codes(), list):
        response = {"code": e.get_codes(), "detail": e.get_full_details()}
    elif isinstance(e.get_codes(), dict) and "non_field_errors" in e.get_codes().keys():
        response = {
            "code": e.get_codes()["non_field_errors"],
            "detail": e.get_full_details(),
        }

    else:
        response = {"code": ["CODE0"], "detail": e.get_full_details()}

    return response
