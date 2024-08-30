from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson
from django.utils.translation import gettext as _

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):
    class PaymentMethodChoices(models.TextChoices):
        CASH = 'Наличные', _('Наличные')
        CARD = 'Карта', _('Карта')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма платежа')
    payment_method = models.CharField(default=PaymentMethodChoices.CASH, choices=PaymentMethodChoices,
                                      verbose_name='Способ оплаты')

    def __str__(self):
        return (f"{self.user} | {self.payment_date} | {self.payment_amount} | {self.payment_method} | "
                f"{self.paid_course if self.paid_course else self.paid_lesson}")

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ['-payment_date', ]
