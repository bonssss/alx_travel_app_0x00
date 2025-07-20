from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create or get a test user
        user, created = User.objects.get_or_create(username='testhost', defaults={'email': 'testhost@example.com'})

        for i in range(10):
            Listing.objects.create(
                title=f"Sample Listing {i+1}",
                description="A wonderful place to stay.",
                price_per_night=random.uniform(50, 300),
                host=user
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))
