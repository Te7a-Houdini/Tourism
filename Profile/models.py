from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Users(AbstractUser):
    blk_flg = models.BooleanField(default=False)

#
# class Users(AbstractUser):
#     blk_flg = models.BooleanField(default=False)
