from rest_framework import serializers
from .models import Games

import random

class GamesSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    class Meta(object):
        model = Games
        fields = ('id', 'name', 'price', 'space')
        
    