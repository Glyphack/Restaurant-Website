from django.test import TestCase
from .models import User, Customer
# Create your tests here.
def create_customer(username, password, first_name, last_name, address):
    user1 = User(username, password, first_name, last_name)
    customer = Customer(user = user1, address = 'test address')