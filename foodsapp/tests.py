from django.test import TestCase
from django.urls import reverse
from foodsapp.models import Food
# Create your tests here.

def create_food(name, details, likes, price, ordered_times):
    """
    Create a food with name and details given
    """
    return Food.objects.create(name=name, details=details, likes=likes, price=price, ordered_times=ordered_times, picture='test.png')

class FoodsAppIndexViewTests(TestCase):
    def test_if_page_loads_currectly(self):
        """
        should be able to reach /
        """
        response = self.client.get(reverse('foodsapp:index'))
        self.assertEqual(response.status_code, 200)

class FoodsAppMenuViewTests(TestCase):
    def test_if_page_loads_currectly(self):
        """
        should be able to reach /foods
        """
        response = self.client.get(reverse('foodsapp:menu'))
        self.assertEqual(response.status_code, 200)

    def test_if_page_shows_food(self):
        create_food(name='chicken',details='good', likes=11, price=5, ordered_times=1)
        response = self.client.get(reverse('foodsapp:menu'))
        self.assertQuerysetEqual(response.context['foods'],['<Food: chicken>'])

    def test_if_page_shows_multiple_foods(self):
        create_food(name='chicken',details='good', likes=11, price=5, ordered_times=1)
        create_food(name='pizza',details='yummy!', likes=1, price=2, ordered_times=3)
        response = self.client.get(reverse('foodsapp:menu'))
        self.assertQuerysetEqual(response.context['foods'],['<Food: chicken>','<Food: pizza>'])