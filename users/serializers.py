from rest_framework import serializers
from users.models import User, Payments, Subscription
from users.services import retrieve_strip_session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'phone', 'email', 'is_superuser', 'is_staff', 'is_active']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class UserNotOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'is_active']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['id', 'name', 'last_name', 'phone', 'email', 'is_superuser', 'is_staff', 'is_active', 'payments_list']


class PaymentsStatusSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        exclude = ['payment_link', ]

    def get_payment_status(self, instance):
        return retrieve_strip_session(instance.payment_id)


class UserDetailSerializer(serializers.ModelSerializer):
    payments_list = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'phone', 'email''is_superuser', 'is_staff', 'is_active',
                  'payments_list']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
