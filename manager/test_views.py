from django.test import TestCase
from .models import Item


# Create your tests here.

class TestViews(TestCase):
    """[Testing views]"""

    def test_get_manager_lists(self):
        """[return a successful manager_list HTTP response]"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manager/manager_list.html')
        
    def test_get_add_item(self):
        """[return a successful add_item HTTP response]"""
        response = self.client.get('/add', {'task': 'Test', 'owner':'Tester', 'due_date':'2021-05-19T01:55:10+0000', 'done':'True'}, True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manager/add_item.html')

    def test_get_edit_item(self):
        """[return a successful edit_item HTTP response]"""
        item = Item.objects.create(task='Test', owner="Tester", due_date="2021-05-19T01:55:10+0000", done=True)
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manager/edit_item.html')
        
    def test_can_add_item(self):
        """[test if test can add item]"""
        response = self.client.post('/add/', {'task': 'Test', 'owner':'Tester', 'due_date':'2021-05-19T01:55:10+0000', 'done':'True'})
        self.assertRedirects(response, '/')

        
    def test_can_delete_item(self):
        """[test if test can delete item]"""
        item = Item.objects.create(task='Test', owner="Tester", due_date="2021-05-19T01:55:10+0000", done=True)
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
        
    def test_can_toggle_item(self):
        """[test if test can toggle item]"""
        item = Item.objects.create(task='Test', owner="Tester", due_date="2021-05-19T01:55:10+0000", done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        """[test if test can edit item]"""
        item = Item.objects.create(task='Test', owner="Tester", due_date="2021-05-19T01:55:10+0000", done=True)
        response = self.client.post(f'/edit/{item.id}', {'task': 'Updated task', 'owner':'Tester 2', 'due_date':'2021-05-19T01:55:10+0000', 'done':'True'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.task, 'Updated task')
        self.assertEqual(updated_item.owner, 'Tester 2')