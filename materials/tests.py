from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="test@example.com", password="test123qwe")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Курс 1", description="Тестовый курс 1", owner=self.user)
        self.lesson = Lesson.objects.create(title="Урок 1", description="Тестовый урок 1",
                                            url="https://youtube.com/123", course=self.course, owner=self.user)

    def test_lesson_create(self):
        # Валидные данные
        data_valid = {
            "title": "Урок 2",
            "description": "Описание урока 2",
            "url": "https://youtube.com/444",
            "course": self.course.pk
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data_valid)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "id": 2,
            "title": "Урок 2",
            "description": "Описание урока 2",
            "preview": "http://testserver/media/lesson/image/default_lesson.jpg",
            "url": "https://youtube.com/444",
            "course": self.course.pk,
            "owner": self.user.pk
        })

        # Невалидные данные
        data_invalid = {
            "title": "Урок 2",
            "description": "Описание урока 2",
            "url": "https://site.com",
            "course": self.course.pk
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data_invalid)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['Запрещенная ссылка! Используйте видео с платформы youtube.com']})

    def test_lesson_update(self):
        data = {"title": "Урок",
                "description": "Измененное описание урока",
                "url": "https://youtube.com/123",
                "course": self.course.pk}

        response = self.client.patch(reverse('materials:lesson_update', kwargs={'pk': self.lesson.pk}),
                                     data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "id": self.lesson.pk,
            "title": "Урок",
            "description": "Измененное описание урока",
            "preview": "http://testserver/media/lesson/image/default_lesson.jpg",
            "url": "https://youtube.com/123",
            "course": self.course.pk,
            "owner": self.user.pk
        })

    def test_lesson_list(self):
        response = self.client.get(reverse('materials:lesson_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": self.lesson.pk,
                 "title": "Урок 1",
                 "description": "Тестовый урок 1",
                 "preview": "http://testserver/media/lesson/image/default_lesson.jpg",
                 "url": "https://youtube.com/123",
                 "course": self.course.pk,
                 "owner": self.user.pk
                 }
            ]

        })

    def test_lesson_retrieve(self):
        response = self.client.get(reverse('materials:lesson_detail', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "id": self.lesson.pk,
            "title": "Урок 1",
            "description": "Тестовый урок 1",
            "preview": "http://testserver/media/lesson/image/default_lesson.jpg",
            "url": "https://youtube.com/123",
            "course": self.course.pk,
            "owner": self.user.pk
        })

    def test_lesson_destroy(self):
        response = self.client.delete(reverse('materials:lesson_delete', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.all().exists())
