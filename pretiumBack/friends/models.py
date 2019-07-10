from django.db import models
from userAuth import views
from userAuth.models import User

# Create your models here.

class Friendship(models.Model):
    user1 = models.ForeignKey(verbose_name='First user id', to=User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(verbose_name='Second user id', to=User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(verbose_name='friendship status', default=0)