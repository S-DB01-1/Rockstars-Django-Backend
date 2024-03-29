import logging
import random
import string

from rest_framework import status
from rest_framework.test import APITestCase

from tribe import models

logger = logging.getLogger(__name__)


def random_string():
    # Returns a random string of 12 lowercase characters.
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(12))


def get_request_json(url, client):
    # Sends a get request to the "url" parameter and returns the response.
    logger.debug('Sending GET request to url: %s' % url)
    response = client.get(url, format='json')
    return response


class TribeViewSetTests(APITestCase):
    def add_test_tribe(self):
        # Adds a test tribe into the database.
        logger.debug('Adding new row with random tribe data into database')

        self.tribe_name = random_string()
        self.tribe_description = random_string()

        t = models.Tribes(Name=self.tribe_name, Description=self.tribe_description)
        t.save()

        logger.debug('Successfully added test tribe into the database')

    def test_get_tribe(self):
        # Test to verify test tribe can be fetched from API.
        logger.debug('Starting test get tribes')

        self.add_test_tribe()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/tribes/1/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether values match')
        self.assertEqual(json['Name'], self.tribe_name)
        self.assertEqual(json['Description'], self.tribe_description)

    def test_list_tribes(self):
        # Test to verify whether multiple tribes are present in the database.
        logger.debug('Starting test list tribes')

        logger.debug('Adding multiple test tribes to database')
        tribe_amount = random.randrange(1, 6)
        for i in range(tribe_amount):
            self.add_test_tribe()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/tribes/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether there are the exact amount of tribes as created')
        self.assertEqual(json['count'], tribe_amount)


class ArticleViewSetTests(APITestCase):
    def add_test_article(self):
        logger.debug('Adding new row with random article data into database')

        self.article_name = random_string()
        self.article_description = random_string()

        a = models.Articles(Name=self.article_name, Description=self.article_description)
        a.save()

        logger.debug('Successfully added test article into the database')

    def test_get_article(self):
        # Test to verify test article can be fetched from API.
        logger.debug('Starting test get tribes')

        self.add_test_article()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/articles/1/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether values match')
        self.assertEqual(json['Name'], self.article_name)
        self.assertEqual(json['Description'], self.article_description)

        logger.debug('Testing if viewcount works.')
        response = get_request_json(url='http://127.0.0.1:8000/api/v1/articles/1/?format=json', client=self.client)
        json = response.json()
        view_count = json['Viewcount']

        self.assertEqual(view_count, 1)

    def test_list_articles(self):
        # Test to verify whether multiple articles are present in the database.
        logger.debug('Starting test list tribes')

        logger.debug('Adding multiple test tribes to database')
        article_amount = random.randrange(1, 6)
        for i in range(article_amount):
            self.add_test_article()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/articles/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether there are the exact amount of tribes as created')
        self.assertEqual(json['count'], article_amount)


class OnDemandRequestsViewSetTests(APITestCase):
    def test_create_ondemandrequest(self):
        # Test to verify if ondemand request can be created by POST request.
        logger.debug('Starting test create ondemand request form')

        url = 'http://127.0.0.1:8000/api/v1/ondemand/'

        self.name = random_string()
        self.email = random_string()
        self.phone_number = random_string()
        self.date = '2022-03-17 10:34:09'
        self.subject = random_string()

        data = {
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'date': self.date,
            'subject': self.subject
        }

        logger.debug('Sending TEST data to url: %s, data: %s' % (url, data))
        response = self.client.post(url, data, format='json')

        # logger.debug('Testing status code response: %s, code: %d' % (response.json(), response.status_code))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        logger.debug('Test ondemand request create completed successfully')

    def test_ondemandrequest_db(self):
        # Test to verify whether the POST JSON values were saved correctly to the db.
        logger.debug('Starting test ondemand request database')

        logger.debug('Create random ondemand request form')
        self.test_create_ondemandrequest()

        logger.debug('Testing person count to make sure object was successfully added')
        self.assertEqual(models.OnDemandRequests.objects.count(), 1)

        logger.debug('Testing new person object details')
        o = models.OnDemandRequests.objects.get(id=1)
        self.assertEqual(o.Name, self.name)
        self.assertEqual(o.PhoneNumber, self.phone_number)
        self.assertEqual(str(o.Date), self.date)
        self.assertEqual(o.Subject, self.subject)


class PodcastsViewSetTests(APITestCase):
    def add_test_tribe(self):
        # Adds a test tribe into the database.
        logger.debug('Adding new row with random tribe data into database')

        self.tribe_name = random_string()
        self.tribe_description = random_string()

        t = models.Tribes(Name=self.tribe_name, Description=self.tribe_description)
        t.save()

        logger.debug('Successfully added test tribe into the database')

    def add_test_podcast(self):
        # Adds a test podcast into the database.
        logger.debug('Adding new row with random podcast data into database')

        self.add_test_tribe()
        self.spotify_url = 'https://open.spotify.com/track/3spdoTYpuCpmq19tuD0bOe?si=6c9f24f42db74580'

        p = models.Podcasts(Tribe_id=1, SpotifyUrl=self.spotify_url)
        p.save()

        logger.debug('Successfully added test podcast into the database')

    def test_get_podcast(self):
        # Test to verify test podcast can be fetched from API.
        logger.debug('Starting test get podcasts')

        self.add_test_podcast()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/podcasts/1/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether values match')
        self.assertEqual(json['SpotifyUrl'], self.spotify_url)

    def test_list_podcasts(self):
        # Test to verify whether multiple podcasts are present in the database.
        logger.debug('Starting test list podcasts')

        logger.debug('Adding multiple test podcasts to database')
        podcast_amount = random.randrange(1, 6)
        for i in range(podcast_amount):
            self.add_test_podcast()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/podcasts/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether there are the exact amount of podcasts as created')
        self.assertEqual(json['count'], podcast_amount)


class VideosViewSetTests(APITestCase):
    def add_test_tribe(self):
        # Adds a test tribe into the database.
        logger.debug('Adding new row with random tribe data into database')

        self.tribe_name = random_string()
        self.tribe_description = random_string()

        t = models.Tribes(Name=self.tribe_name, Description=self.tribe_description)
        t.save()

        logger.debug('Successfully added test tribe into the database')

    def add_test_video(self):
        # Adds a test video into the database.
        logger.debug('Adding new row with random video data into database')

        self.add_test_tribe()
        self.video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

        t = models.Videos(Tribe_id=1, VideoUrl=self.video_url)
        t.save()

        logger.debug('Successfully added test video into the database')

    def test_get_video(self):
        # Test to verify test video can be fetched from API.
        logger.debug('Starting test get videos')

        self.add_test_video()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/videos/1/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether values match')
        self.assertEqual(json['VideoUrl'], self.video_url)

    def test_list_videos(self):
        # Test to verify whether multiple videos are present in the database.
        logger.debug('Starting test list videos')

        logger.debug('Adding multiple test videos to database')
        video_amount = random.randrange(1, 6)
        for i in range(video_amount):
            self.add_test_video()

        response = get_request_json(url='http://127.0.0.1:8000/api/v1/videos/?format=json', client=self.client)
        json = response.json()

        logger.debug('Testing status code response: %s, code: %d' % (json, response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        logger.debug('Testing whether there are the exact amount of videos as created')
        self.assertEqual(json['count'], video_amount)
