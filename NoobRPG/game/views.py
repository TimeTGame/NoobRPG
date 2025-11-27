__all__ = ()

from entities.models import NonPlayerCharacter as NPCModel
from entities.models import Player
from locations.models import Location
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class ChangeLocationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data

        location_id = data.get('location_id')
        player_id = data.get('player_id')

        if not location_id:
            return Response({'error': 'Location ID is required'}, status=400)

        try:
            location_id = int(location_id)
            if location_id <= 0:
                return Response(
                    {'error': 'Location ID must be a positive integer'},
                    status=400,
                )
        except (ValueError, TypeError):
            return Response(
                {'error': 'Location ID must be a valid integer'},
                status=400,
            )

        if player_id:
            try:
                player_id = int(player_id)
                if player_id <= 0:
                    return Response(
                        {'error': 'Player ID must be a positive integer'},
                        status=400,
                    )
            except (ValueError, TypeError):
                return Response(
                    {'error': 'Player ID must be a valid integer'},
                    status=400,
                )

        try:
            if player_id:
                player = Player.objects.get(id=player_id, user=request.user)
            else:
                player = Player.objects.get(user=request.user)

            location = Location.objects.get(id=location_id)

            player.current_location = location
            player.save()

            return Response(
                {
                    'message': (
                        f'Location updated successfully to {location.name}'
                    ),
                    'current_location': location.name,
                    'location_id': location.id,
                    'player_id': player.id,
                },
            )

        except Player.DoesNotExist:
            return Response(
                {
                    'error': (
                        'Player not found. Either the player does not exist '
                        'or you do not have permission to update this player.',
                    ),
                },
                status=404,
            )
        except Location.DoesNotExist:
            return Response({'error': 'Location not found'}, status=404)
        except Exception as e:
            print(f'Error updating player location: {e}')
            return Response(
                {'error': 'An error occurred while updating the location'},
                status=500,
            )


class StartBattleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data

        npc_id = data.get('npc_id')
        player_id = data.get('player_id')

        if not npc_id:
            return Response({'error': 'NPC ID is required'}, status=400)

        try:
            npc_id = int(npc_id)
            if npc_id <= 0:
                return Response(
                    {'error': 'NPC ID must be a positive integer'},
                    status=400,
                )
        except (ValueError, TypeError):
            return Response(
                {'error': 'NPC ID must be a valid integer'},
                status=400,
            )

        if player_id:
            try:
                player_id = int(player_id)
                if player_id <= 0:
                    return Response(
                        {'error': 'Player ID must be a positive integer'},
                        status=400,
                    )
            except (ValueError, TypeError):
                return Response(
                    {'error': 'Player ID must be a valid integer'},
                    status=400,
                )

        try:
            if player_id:
                player = Player.objects.get(id=player_id, user=request.user)
            else:
                player = Player.objects.get(user=request.user)

            npc = NPCModel.objects.get(id=npc_id)

            player.is_in_battle = True
            npc.is_in_battle = True
            player.save()
            npc.save()

            return Response(
                {
                    'message': f'You are now in battle with {npc.name}',
                    'player is in battle': player.is_in_battle,
                    'NPC is in battle': npc.is_in_battle,
                    'npc_id': npc.id,
                    'player_id': player.id,
                },
            )

        except Player.DoesNotExist:
            return Response(
                {
                    'error': (
                        'Player not found. Either the player does not exist '
                        'or you do not have permission to update this player.',
                    ),
                },
                status=404,
            )
        except NPCModel.DoesNotExist:
            return Response({'error': 'NPC not found'}, status=404)
        except Exception as e:
            print(f'Error updating player is_in_battle: {e}')
            return Response(
                {'error': 'An error occurred while starting battle'},
                status=500,
            )


class AttackView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data

        npc_id = data.get('npc_id')
        player_id = data.get('player_id')

        if not npc_id:
            return Response({'error': 'NPC ID is required'}, status=400)

        try:
            npc_id = int(npc_id)
            if npc_id <= 0:
                return Response(
                    {'error': 'NPC ID must be a positive integer'},
                    status=400,
                )
        except (ValueError, TypeError):
            return Response(
                {'error': 'NPC ID must be a valid integer'},
                status=400,
            )

        if player_id:
            try:
                player_id = int(player_id)
                if player_id <= 0:
                    return Response(
                        {'error': 'Player ID must be a positive integer'},
                        status=400,
                    )
            except (ValueError, TypeError):
                return Response(
                    {'error': 'Player ID must be a valid integer'},
                    status=400,
                )

        try:
            if player_id:
                player = Player.objects.get(id=player_id, user=request.user)
            else:
                player = Player.objects.get(user=request.user)

            if player.is_in_battle is False:
                return Response(
                    {'error': 'First we need to start the battle'},
                    status=400,
                )

            npc = NPCModel.objects.get(id=npc_id)

            if npc.is_in_battle is False:
                return Response(
                    {'error': 'NPC is_in_battle must be True'},
                    status=400,
                )

            player_attack_res = player.attack(npc)
            npc_attack_res = npc.attack(player)

            return Response(
                {
                    'message': f'{player_attack_res} {npc_attack_res}',
                    'player is in battle': player.is_in_battle,
                    'NPC is in battle': npc.is_in_battle,
                    'npc_id': npc.id,
                    'player_id': player.id,
                },
            )

        except Player.DoesNotExist:
            return Response(
                {
                    'error': (
                        'Player not found. Either the player does not exist '
                        'or you do not have permission to update this player.',
                    ),
                },
                status=404,
            )
        except NPCModel.DoesNotExist:
            return Response({'error': 'NPC not found'}, status=404)
        except Exception as e:
            print(f'Error updating player is_in_battle: {e}')
            return Response(
                {'error': 'An error occurred while starting battle'},
                status=500,
            )
