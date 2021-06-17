from django.test import TestCase, Client
from django.urls import reverse

from lost_and_found_app.models import Post, Object


class TestIndex(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_whenNoObjects_shouldRenderCorrectTemplateWithNoObjects(self):
        response = self.test_client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        obj = response.context['posts']
        self.assertEqual(0, len(obj))

    def test_getIndex_whenObjects_shouldRenderCorrectTemplateWithObjects(self):
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
            Post(title='phone', description='broken',author_phone='0878799823',author_name='Bobby', object=obj),
            Post(title='phone2', description='new', author_phone='0878799823', author_name='Borcho', object=obj),
        )
        [post.save() for post in all_posts]

        response = self.test_client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        all_posts = response.context['posts']
        self.assertEqual(2, len(all_posts))

