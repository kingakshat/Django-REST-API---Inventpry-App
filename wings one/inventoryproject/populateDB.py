import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventoryproject.settings')
django.setup()

from inventortapp.models import Inventory

# Initialize Faker
fake = Faker()

# Function to generate random data for Inventory model
def populate_inventory(n):
    for _ in range(n):
        name = fake.word().capitalize()
        category = 'object' #fake.word().capitalize()
        price = random.randint(10, 1000)
        quantity = random.randint(1, 100)
        barcode = fake.unique.random_int(min=100000, max=999999)

        Inventory.objects.create(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            barcode=barcode
        )

# Generate 10 random inventory items
populate_inventory(10)

print("Successfully populated inventory with random data.")
