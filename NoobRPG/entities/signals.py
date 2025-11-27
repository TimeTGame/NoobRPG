__all__ = ()

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from entities.models import Player
from locations.models import Location


@receiver(post_save, sender=User)
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'player_profile'):
            default_location = Location.objects.first()

            if default_location:
                Player.objects.create(
                    user=instance,
                    name=instance.username,
                    start_location=default_location,
                    hp=100,
                    max_hp=100,
                    mana=20,
                    max_mana=20,
                    base_damage=10,
                    current_location=default_location,
                    is_in_battle=False,
                )
            else:
                default_location = Location.objects.create(
                    name='Default Location',
                    slug='default-location',
                )
                Player.objects.create(
                    user=instance,
                    name=instance.username,
                    start_location=default_location,
                    hp=100,
                    max_hp=100,
                    mana=20,
                    max_mana=20,
                    base_damage=10,
                    current_location=default_location,
                    is_in_battle=False,
                )


@receiver(post_save, sender=User)
def save_player_profile(sender, instance, **kwargs):
    if hasattr(instance, 'player_profile'):
        instance.player_profile.save()
