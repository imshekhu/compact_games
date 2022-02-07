from urllib import response
from django.urls import reverse
from api.models import Games

from rest_framework import status
from rest_framework.test import APITestCase


class GamesTests(APITestCase):
    """
    Generate tests on apis 
    Args:
        APITestCase ([type]): [description]
    """
    @classmethod
    def setUpTestData(cls):
        Games.objects.create(name="Valorant",price=1,space=120)

    
    def test_create_games(self):
        """
        Ensure we can create a new game object.
        """
        url = reverse('api:create-games')
        data = {
            "name":"test1", 
            "price":1,
            "space":130
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_db_connection(self):
        """
        Ensure the db connection
        """
        url = reverse('api:db-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_best_value_games(self):
        """
        fetch best value games
        """
        url = reverse('api:best-value-games') + '?pen_drive_space=150'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    