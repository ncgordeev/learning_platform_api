from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from materials.models import Course
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="test@example.com", password="test123qwe")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Курс", description="Тестовый курс", owner=self.user)
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)

    def test_subscription(self):
        data = {"user": self.user.pk,
                "course": self.course.pk}

        response = self.client.post(reverse('users:subscribe'), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка удалена"})

        response = self.client.post(reverse('users:subscribe'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка добавлена"})
