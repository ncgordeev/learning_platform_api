from rest_framework import serializers


class LinkValidator:
    """Класс валидатор корректности ссылки"""
    YOUTUBE = 'youtube.com'

    def __init__(self, field):
        self.link = field

    def __call__(self, *args, **kwargs):
        if self.YOUTUBE not in self.link.lower():
            raise serializers.ValidationError("Запрещенная ссылка! Используйте видео с платформы youtube.com")
