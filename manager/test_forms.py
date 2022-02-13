from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """[Testing form]"""

    def test_item_task_is_required(self):
        """[Input test]"""
        form = ItemForm({'task': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('task', form.errors.keys())
        self.assertEqual(form.errors['task'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """[Test if field is required]"""
        form = ItemForm({'task': 'Test manager Item'})
        self.assertFalse(form.is_valid())

    def test_fields_are_expilcit_in_the_form_metaclass(self):
        """[Test if fields are defined explicitly]"""
        form = ItemForm()
        self.assertEqual(form.Meta.fields, [
                         'task', 'owner', 'due_date', 'done'])
