from django.test import TestCase

from lost_and_found_app.forms import PostEditForm


class TestPostEditForm(TestCase):

    def test_saveForm_whenValidEdit_shouldBeValid(self):
        data_old = {
            'title': 'phone 2',
            'description': 'broken',
            'author_name': 'Bobby',
            'author_phone': "0877558556",
            'found': bool
        }
        form = PostEditForm(data_old)

        self.assertTrue(form.is_valid())
