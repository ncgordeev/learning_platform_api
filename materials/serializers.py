from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import LinkValidator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True)
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_count_lesson(course):
        return Lesson.objects.filter(course=course).count()

    def get_subscribe(self, course):
        user = self.context['request'].user
        if Subscription.objects.filter(course=course, user=user):
            return f"Вы подписаны на курс"
