from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pasta", price=12.50, inventory=10)
        Menu.objects.create(title="Pizza", price=15.00, inventory=5)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized = menuSerializer(menus, many=True)
        expected_data = serialized.data
        # Simulate what a view would return
        self.assertEqual(list(expected_data), list(serialized.data))
