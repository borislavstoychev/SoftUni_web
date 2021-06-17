from django.test import TestCase

from lost_and_found_app.forms import ObjectForm


class TestObjectForm(TestCase):

    def test_saveForm_whenValid_shouldBeValid(self):
        name = 'Bobby'
        image = 'https://media.wired.com/photos/5f401ecca25385db776c0c46/master/pass/Gear-How-to-Apple-ios-13-home-screen-iphone-xs-06032019_big_large_2x.jpg'
        width = 5
        height = 6
        weight = 8
        form = ObjectForm(data={
            'name': name,
            'image': image,
            'width': width,
            'height': height,
            'weight': weight,
        })

        self.assertTrue(form.is_valid())
