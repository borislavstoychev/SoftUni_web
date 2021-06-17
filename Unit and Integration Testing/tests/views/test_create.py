from django.db import DataError
from django.test import TestCase, Client
from django.urls import reverse


class TestCreate(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_postCreate_whenValidEgn_shouldRedirectToIndex(self):
        data_obj = {
            'name': 'Bobby',
            'image': 'https://media.wired.com/photos/5f401ecca25385db776c0c46/master/pass/Gear-How-to-Apple-ios-13-home-screen-iphone-xs-06032019_big_large_2x.jpg',
            'width': 5,
            'height': 6,
            'weight': 8,
            'title': 'phone2',
            'description': 'new',
            'author_phone': '0878799823',
            'author_name': 'Borcho',
            }
        response = self.test_client.post(reverse('create'), data=data_obj)

        self.assertRedirects(response, reverse('index'))

    def test_getCreate_whenValidEgn_shouldRedirectToIndex(self):
        response = self.test_client.get(reverse('create'))
        self.assertTemplateUsed(response, 'post_create.html')
        form = response.context['post_form']
        self.assertIsNotNone(form)

    def test_postCreate_whenInvalidEgn_shouldRedirectToCreate(self):
        data_obj = {
            'name': 'Bobby',
            'image': 'https://media.wired.com/photos/5f401ecca25385db776c0c46/master/pass/Gear-How-to-Apple-ios-13-home-screen-iphone-xs-06032019_big_large_2x.jpg',
            'width': 5,
            'height': 6,
            'weight': 8,
            'title': 'phone2',
            'description': 'new',
            'author_phone': '0878799823kjjhjk',
            'author_name': 'Borcho',
            }
        try:
            response = self.test_client.post(reverse('create'), data=data_obj)
        except DataError:
            self.assertTemplateUsed('post_creat.html')
