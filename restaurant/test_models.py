from django.test import TestCase
from restaurant.models import MenuItem, Booking, Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_get_item_method(self):
        item = MenuItem.objects.create(title="Pizza", price=50, inventory=20)
        self.assertEqual(item.get_item(), "Pizza : 50")

    def test_inventory_field(self):
        item = MenuItem.objects.create(title="Soup", price=20, inventory=5)
        self.assertEqual(item.inventory, 5)

    def test_price_field(self):
        item = MenuItem.objects.create(title="Salad", price=30, inventory=10)
        self.assertEqual(item.price, 30)

class BookingTest(TestCase):
    def test_booking_str_fields(self):
        booking = Booking.objects.create(id=1, name="John Doe", no_of_guests=4, bookingdate="2025-05-24")
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(str(booking.bookingdate), "2025-05-24")

class MenuTest(TestCase):
    def test_menu_str_fields(self):
        menu = Menu.objects.create(id=1, title="Burger", price=9.99, inventory=15)
        self.assertEqual(menu.title, "Burger")
        self.assertEqual(menu.price, 9.99)
        self.assertEqual(menu.inventory, 15)
        # If Menu has __str__, test it as well
        self.assertEqual(str(menu), "Burger")
