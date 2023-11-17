from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from projects.models import Project, ProjectMember, Cart, Task
from faker import Faker
import random

fake = Faker()
User = get_user_model()


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting population...'))

        # Create some users
        for _ in range(5):
            User.objects.create_user(username=fake.user_name(), password="password")

        users = User.objects.all()

        # Create some projects
        for _ in range(3):
            project = Project.objects.create(
                title=fake.word(),
                description=fake.text(),
                owner=random.choice(users)
            )

            # Add some members to the project
            for _ in range(3):
                ProjectMember.objects.create(
                    project=project,
                    user=random.choice(users)
                )

        # Create some carts and tasks
        for project in Project.objects.all():
            for _ in range(2):
                cart = Cart.objects.create(
                    title=fake.word(),
                    project=project
                )

                for _ in range(3):
                    Task.objects.create(
                        title=fake.sentence(),
                        comment=fake.paragraph(),
                        cart=cart
                    )

        self.stdout.write(self.style.SUCCESS('Population completed successfully.'))
