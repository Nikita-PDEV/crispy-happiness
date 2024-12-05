from rest_framework.test import APITestCase  
from rest_framework import status  
from .models import Pereval, Coords  

class PerevalAPITests(APITestCase):  
    def setUp(self):  
        self.valid_data = {  
            "beauty_title": "Лучший перевал",  
            "title": "Перевал 1",  
            "other_titles": "Другие названия",  
            "connect": "Дорога ведет через горы",  
            "coord": {  
                "latitude": 40.0,  
                "longitude": 70.0,  
                "height": 2500  
            },  
            "status": "active"  
        }  
        
    def test_submit_data(self):  
        response = self.client.post('/pereval/submitData/', data=self.valid_data, format='json')  
        print("Ответ сервера:", response.data)   
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertTrue(Pereval.objects.filter(title="Перевал 1").exists())  

    def test_submit_invalid_data(self):  
        invalid_data = self.valid_data.copy()  
        invalid_data['coord']['latitude'] = None  # Invalid data  
        response = self.client.post('/pereval/submitData/', data=invalid_data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)