from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from materials.models import Course
from users.models import User, Payments, Subscription
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, PaymentsSerializer, UserDetailSerializer, UserRegisterSerializer, \
    UserNotOwnerSerializer
from rest_framework import generics, views


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserDetailSerializer
        else:
            return UserNotOwnerSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsOwnerOrReadOnly]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('payment_date',)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class SubscribeAPIView(views.APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'
        return Response({"message": message})
