import json

from django.test import TestCase
from django.urls import reverse
#import django.urls import reverse

from myApp.models import Production

class test_production(TestCase):

    @classmethod
    def setUpTestData(cls):
        Production.objects.create(
            title = 'The Godfather',
            description = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            genre = 'Crime, Drama',
            duration = '175 min',
            director = 'Francis Ford Coppola',
            country = 'USA',
            cast = 'Marlon Brando, Al Pacino, James Caan',
            release = '1972-03-24',
            trailer = 'https://www.youtube.com/watch?v=sY1S34973zA',
            platform = 'Netflix'
        )

    def test_view_production(self):
        response = self.client.get('/myApp/readInfo')
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)

    def test_create_production(self):
        response = self.client.post('/myApp/createInfo', data={
            'title': 'The Godfather',
            'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            'genre': 'Crime, Drama',
            'duration': '175 min',
            'director': 'Francis Ford Coppola',
            'country': 'USA',
            'cast': 'Marlon Brando, Al Pacino, James Caan',
            'release': '1972-03-24',
            'trailer': 'https://www.youtube.com/watch?v=sY1S34973zA',
            'platform': 'Netflix'
        })

        self.assertIn(response.status_code, [200, 201])
        filtered_production = Production.objects.filter(title='The Godfather').first()
        self.assertEqual(filtered_production.country, 'USA')

    def test_update_production(self):
        my_production = Production.objects.create(
            title = 'The Godfather',
            description = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            genre = 'Crime, Drama',
            duration = '175 min',
            director = 'Francis Ford Coppola',
            country = 'USA',
            cast = 'Marlon Brando, Al Pacino, James Caan',
            release = '1972-03-24',
            trailer = 'https://www.youtube.com/watch?v=sY1S34973zA',
            platform = 'Netflix'
        )

        valid_production = {
            'title': 'The Godfather',
            'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            'genre': 'Crime, Drama',
            'duration': '175 min',
            'director': 'Francis Ford Coppola',
            'country': 'USA',
            'cast': 'Marlon Brando, Al Pacino, James Caan',
            'release': '1972-03-24',
            'trailer': 'https://www.youtube.com/watch?v=sY1S34973zA',
            'platform': 'Netflix'
        }

        url = reverse('update_info', kwargs={'pk': my_production.id})
        valid_production_json = json.dumps(valid_production)
        response = self.client.put(url, valid_production_json, content_type='application/json')
        self.assertIn(response.status_code, [200, 201])

    def test_delete_production(self):
        my_production = Production.objects.create(
            title = 'The Godfather',
            description = 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            genre = 'Crime, Drama',
            duration = '175 min',
            director = 'Francis Ford Coppola',
            country = 'USA',
            cast = 'Marlon Brando, Al Pacino, James Caan',
            release = '1972-03-24',
            trailer = 'https://www.youtube.com/watch?v=sY1S34973zA',
            platform = 'Netflix'
        )

        url = reverse('delete_info', kwargs={'pk': my_production.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
    