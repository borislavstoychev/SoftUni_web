from django.test import TestCase

from lost_and_found_app.models import Post, Object


class TestPost(TestCase):
    def test_saveModel_whenValid_shouldBeValid(self):
        data_obj = {
            'name': 'Bobby',
            'image': 'https://media.wired.com/photos/5f401ecca25385db776c0c46/master/pass/Gear-How-to-Apple-ios-13-home-screen-iphone-xs-06032019_big_large_2x.jpg',
            'width': 5,
            'height': 6,
            'weight': 8,
        }
        obj = Object(**data_obj)
        obj.save()
        data_post = {
            'title': 'phone 2',
            'description': 'broken',
            'author_name': 'Bobby',
            'author_phone': "0877558556",
            'found': False,
            'object': obj
        }
        post = Post(**data_post)
        post.full_clean()
        post.save()
