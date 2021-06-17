from django.test import TestCase

from lost_and_found_app.models import Object


class TestObject(TestCase):

    def test_saveModel_whenValid_shouldBeValid(self):
        data = {
            'name': 'Bobby',
            'image': 'https://media.wired.com/photos/5f401ecca25385db776c0c46/master/pass/Gear-How-to-Apple-ios-13-home-screen-iphone-xs-06032019_big_large_2x.jpg',
            'width': 5,
            'height': 6,
            'weight': 8,
        }
        obj = Object(**data)
        obj.full_clean()
        obj.save()
