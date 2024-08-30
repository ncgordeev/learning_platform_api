import os
from django.core.management import BaseCommand
from dotenv import load_dotenv
from users.models import User
from config.settings import BASE_DIR

dotenv_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('ADMIN_EMAIL'),
            name='Admin',
            last_name='Root',
            is_staff=True,
            is_superuser=True
        )
        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()
