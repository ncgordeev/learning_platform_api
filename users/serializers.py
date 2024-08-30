from rest_framework import serializers
from users.models import User, Payments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone', 'email', 'is_staff']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    payments_list = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone', 'email', 'is_staff', 'payments_list']
