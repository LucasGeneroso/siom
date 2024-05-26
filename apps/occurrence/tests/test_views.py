from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
from django.contrib.auth.models import User

from apps.occurrence.models import Occurrence


class TestOccurrenceViewSet(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="user_teste", email="test@test.com", password="teste123")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh_token.access_token}")
        Occurrence.objects.create(type="broken_cable", city="Cidade Teste", state="Estado Teste", neighborhood="Bairro Teste",
                                  street="Rua Teste", number=123, description="Descrição de teste", reported_by="Anônimo")

    def test_list_view(self):
        response = self.client.get("/siom/api/occurrences/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = response.json()
        self.assertIsInstance(content, list)

        expected_type = "broken_cable"
        expected_city = "Cidade Teste"
        expected_state = "Estado Teste"
        expected_neighborhood = "Bairro Teste"
        expected_street = "Rua Teste"
        expected_number = 123
        expected_description = "Descrição de teste"
        expected_reported_by = "Anônimo"
        content_data = content[0]
        self.assertEqual(expected_type, content_data.get("type"))
        self.assertEqual(expected_city, content_data.get("city"))
        self.assertEqual(expected_state, content_data.get("state"))
        self.assertEqual(expected_neighborhood, content_data.get("neighborhood"))
        self.assertEqual(expected_street, content_data.get("street"))
        self.assertEqual(expected_number, content_data.get("number"))
        self.assertEqual(expected_description, content_data.get("description"))
        self.assertEqual(expected_reported_by, content_data.get("reported_by"))

    def test_create_view(self):
        data = {
            "type": "fallen_tree",
            "city": "Cidade Teste 2",
            "state": "Estado Teste 2",
            "neighborhood": "Bairro Teste 2",
            "street": "Rua Teste 2",
            "number": 456,
            "description": "Descrição de teste 2",
            "reported_by": "Anônimo 2"
        }

        response = self.client.post("/siom/api/occurrences/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        occurrence_id = 1

        response = self.client.get(f"/siom/api/occurrences/{occurrence_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_type = "broken_cable"
        expected_city = "Cidade Teste"
        expected_state = "Estado Teste"
        expected_neighborhood = "Bairro Teste"
        expected_street = "Rua Teste"
        expected_number = 123
        expected_description = "Descrição de teste"
        expected_reported_by = "Anônimo"
        content = response.json()
        self.assertEqual(expected_type, content.get("type"))
        self.assertEqual(expected_city, content.get("city"))
        self.assertEqual(expected_state, content.get("state"))
        self.assertEqual(expected_neighborhood, content.get("neighborhood"))
        self.assertEqual(expected_street, content.get("street"))
        self.assertEqual(expected_number, content.get("number"))
        self.assertEqual(expected_description, content.get("description"))
        self.assertEqual(expected_reported_by, content.get("reported_by"))
