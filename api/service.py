from typing import Dict
from .models import Games
from .serializer import GamesSerializer
from rest_framework import status

from django.db.models import Sum
from django.db.models import F

class GamesService ():

    def create(self, request )->Dict:
        """
        Create a Game.
        """
        # self.validate_data(request.data)

        serializer = GamesSerializer(data=request.data)

        if serializer.is_valid ():
            serializer.save ()
            return ({"data": serializer.data, "code": status.HTTP_201_CREATED, "message": "Game Created"})

        # if not valid
        return ({"data": serializer.errors, "code": status.HTTP_400_BAD_REQUEST, "message": "Bad Request"})
    
    def get_best_value(self, request) -> Dict:
        """
        Args:
            request ([type]): [description]

        Returns:
            Dict: [description]
        """
        des_space = request.query_params.get('pen_drive_space')
        queryset = Games.objects.filter(
            space__lt=des_space
            ).order_by('-price','space').annotate(
                        space_total=Sum(F('space'))
                        )
        while queryset.aggregate(Sum('space'))['space__sum'] > int(des_space):
            temp = queryset.last()
            queryset = queryset.exclude(id = temp.id)
            
        serializer = GamesSerializer(queryset, many=True)
        return ({"games": serializer.data,
                 "code": status.HTTP_201_CREATED,
                 "total_space": int(des_space),
                 "remaining_space": int(des_space)-queryset.aggregate(Sum('space'))['space__sum'] })
        