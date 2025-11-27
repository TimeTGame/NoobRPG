__all__ = ()

from entities.models import Player
from locations.models import Location


def create_player_for_user(user, player_name=None, location=None):
    try:
        player = user.player_profile
        return player
    except AttributeError:
        pass

    name = player_name or user.username

    start_location = location
    if not start_location:
        start_location = Location.objects.first()

    if not start_location:
        raise ValueError('No location available to assign to the new player.')

    player = Player.objects.create(
        user=user,
        name=name,
        start_location=start_location,
        hp=100,
        max_hp=100,
        mana=20,
        max_mana=20,
        base_damage=10,
        current_location=start_location,
        is_in_battle=False,
    )

    return player


def get_or_create_player_for_user(user, player_name=None, location=None):
    try:
        player = user.player_profile
        return player, False
    except AttributeError:
        player = create_player_for_user(user, player_name, location)
        return player, True
