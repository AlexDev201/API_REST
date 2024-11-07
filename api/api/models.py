from django.db import models

# Create your models here.
class Programmer(models.Model):
    full_name=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100)
    age=models.PositiveBigIntegerField(default=0)
    is_active=models.BooleanField(default=True)