from unittest.mock import patch

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Case, CasePerson


class CaseAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="judge1")
        self.case = Case.objects.create(number="C-001", title="State vs. Doe")
        CasePerson.objects.create(case=self.case, person=self.user, role="judge")

    def test_list_cases_includes_parties(self):
        url = reverse("case-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["number"], "C-001")
        self.assertEqual(
            response.data[0]["parties"],
            [{"id": 1, "person": "judge1", "role": "judge"}],
        )

    @patch("cases.views.hello_message.send")
    def test_create_case(self, mock_hello_send):
        url = reverse("case-list")
        response = self.client.post(url, {"number": "C-002", "title": "New Case"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Case.objects.filter(number="C-002").exists())
        mock_hello_send.assert_called_once_with()

    def test_update_case_status(self):
        url = reverse("case-detail", args=[self.case.pk])
        response = self.client.patch(url, {"status": "hearing"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.case.refresh_from_db()
        self.assertEqual(self.case.status, Case.Status.HEARING)

    def test_delete_case(self):
        url = reverse("case-detail", args=[self.case.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Case.objects.filter(pk=self.case.pk).exists())
