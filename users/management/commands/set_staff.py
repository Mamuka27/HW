from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Set is_staff=True for all users'

    def handle(self, *args, **kwargs):
        updated = CustomUser.objects.update(is_staff=True)
        self.stdout.write(self.style.SUCCESS(f'Successfully set is_staff=True for {updated} users.'))
