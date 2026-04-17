from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == "your_app_name":
        Group.objects.get_or_create(name="Managers")
        Group.objects.get_or_create(name="Editors")

