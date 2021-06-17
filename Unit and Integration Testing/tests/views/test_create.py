from django.db import DataError
from django.test import TestCase, Client
from django.urls import reverse

from lost_and_found_app.models import Object, Post


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

    def test_postEdit_shouldRedirectToIndex(self):
        data_obj = {
            'name': 'Bobby',
            'image': 'https://media.wired.com/photos/5f401ecca25385db776c0c46/master/pass/Gear-How-to-Apple-ios-13-home-screen-iphone-xs-06032019_big_large_2x.jpg',
            'width': 5,
            'height': 6,
            'weight': 8,
        }
        obj = Object(**data_obj)
        obj.save()
        all_posts = (
            Post(title='phone', description='broken', author_phone='0878799823', author_name='Bobby', object=obj),
            Post(title='phone2', description='new', author_phone='0878799823', author_name='Borcho', object=obj),
        )
        [post.save() for post in all_posts]
        data = all_posts[0].id
        response = self.test_client.post(reverse(f'edit:{data}'), pk=data)
        self.assertTemplateUsed(response, 'index.html')
        form = response.context['post_form']
        self.assertIsNotNone(form)