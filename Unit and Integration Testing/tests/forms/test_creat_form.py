from django.test import TestCase

from lost_and_found_app.forms import PostCreateForm


class TestPostCreateForm(TestCase):
    def test_saveForm_whenValid_shouldBeValid(self):
        title = 'phone 2'
        description = 'broken'
        author_name = 'Bobby'
        author_phone = "0877558556"
        form = PostCreateForm(data={
            'title': title,
            'description': description,
            'author_name': author_name,
            'author_phone': author_phone
        })

        self.assertTrue(form.is_valid())
