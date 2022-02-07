from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .service import GamesService
from .serializer import GamesSerializer

from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from django.db import connections
from django.db.utils import OperationalError

service = GamesService()

class GameCreateView (APIView):
    """
    Creating a Game
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_description="POST api/v1/games/",  request_body=GamesSerializer)
    def post(self, request:request ):
        """
        Create New Game.
        """
        result = service.create (request )
        return Response (result, status=result["code"])

class BestValueView (APIView):
    q = openapi.Parameter('pen_drive_space', openapi.IN_QUERY, description="100", type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(operation_description="GET /api/best_value_games/", manual_parameters = [q])
    def post(self, request:request ):
        """
        Get Game as List
        """
        result = service.get_best_value(request )
        return Response (result, status=result["code"])
    
class DbStatusView(APIView):
    """
    Get DB Status
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_description="GET api/v1/status/")
    def get(self, request:request):
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            return Response({"database": "unhealthy"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)    
        else:
            return Response({"database": "healthy"}, status=status.HTTP_200_OK)