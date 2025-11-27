__all__ = ()

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from entities.models import NonPlayerCharacter as NPCModel
from entities.views import NPCsViewSet
from locations.models import Location
from rest_framework.test import force_authenticate


class NPCLocationQueryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )

        self.location1 = Location.objects.create(name='Forest', slug='forest')
        self.location2 = Location.objects.create(name='Castle', slug='castle')

        self.npc1 = NPCModel.objects.create(
            name='Forest Guardian',
            current_location=self.location1,
        )
        self.npc2 = NPCModel.objects.create(
            name='Castle Guard',
            current_location=self.location2,
        )

    def test_npc_list_without_query_param(self):
        view = NPCsViewSet.as_view({'get': 'list'})
        request = self.factory.get('/api/v1/entities/npcs/')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_npc_list_with_location_query_param(self):
        view = NPCsViewSet.as_view({'get': 'list'})
        request = self.factory.get(
            '/api/v1/entities/npcs/?current_location__slug=forest',
        )
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Forest Guardian')

    def test_npc_list_with_nonexistent_location(self):
        view = NPCsViewSet.as_view({'get': 'list'})
        request = self.factory.get(
            '/api/v1/entities/npcs/?current_location__slug=nonexistent',
        )
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
