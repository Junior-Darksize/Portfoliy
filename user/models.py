from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class UserTypeEnum(models.TextChoices):
        SELLER = 'seller'
        CUSTOMER = 'customer'
        ADMIN = 'admin'

    user_type = models.CharField(max_length=8,choices=UserTypeEnum.choices,default=UserTypeEnum.CUSTOMER)


class Code(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    code = models.IntegerField()