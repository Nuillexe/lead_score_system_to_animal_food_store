from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os
User = get_user_model()

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if not User.objects.filter(username="admin").exists():
       User.objects.create_superuser(
            username=os.environ.get("ADMIN_USER", "admin"),
            email="admin@email.com",
            password=os.environ.get("ADMIN_PASSWORD", "123456")
        )