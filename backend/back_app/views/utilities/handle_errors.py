from rest_framework import status
from arango import (
    DocumentDeleteError,
    DocumentGetError,
    DocumentInsertError,
)

from rest_framework.serializers import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
import logging
from rest_framework.response import Response
from rest_framework.views import APIView


logger = logging.getLogger("jam")


class HandleError(APIView):
    def handle_error(text):
        def decorator(function):
            def wrapper(*args, **kwargs):
                try:
                    return function(*args, **kwargs)

                except DocumentInsertError as e:
                    logger.error(f"{text}: Except DocumentInsertError : {str(e)}")

                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except DocumentGetError as e:
                    logger.error(f"{text}: Except DocumentGetError : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                except DocumentDeleteError as e:
                    logger.error(f"{text}: Except DocumentDeleteError : {str(e)}")
                    return Response(
                        {"status": "Internal server error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
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

