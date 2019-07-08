from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
