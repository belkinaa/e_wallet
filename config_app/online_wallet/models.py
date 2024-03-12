from django.db import models
from authuser.models import User
# Create your models here.
class Wallet(models.Model):
    CHOICES = (
        ('₽', 'RUB'),
        ('$', 'USD'),
    )
    balance = models.IntegerField(default=0)
    currency = models.CharField(max_length=1, choices=CHOICES, default='RUB')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="walets")

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Электронные кошельки'

    def __str__(self):
        return self.currency
