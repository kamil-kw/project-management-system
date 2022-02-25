from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """[Testing models]"""
    def test_done_defaults_to_false(self):
        """[Testing if manager items will be created by default]"""
        item = Item.objects.create(task='Test',
                                   owner="Tester",
                                   due_date="2021-05-19T01:55:10+0000")
        self.assertFalse(item.done)

    def test_item_string_method_returns_task(self):
        """[Testing if string returns task]"""
        item = Item.objects.create(task='Test',
                                   owner="Tester",
                                   due_date="2021-05-19T01:55:10+0000",
                                   done=True)
        self.assertEqual(str(item), "Test", "Tester")
