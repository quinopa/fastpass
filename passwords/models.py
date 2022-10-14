from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

# Create your models here.
class PasswordModel(models.Model):
    password_user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    password = models.BinaryField(max_length=256)

    def __str__(self):
        return f"{self.password_user.username} -> {self.name}"