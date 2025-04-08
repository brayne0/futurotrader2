from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    id_number = models.CharField(max_length=30)
    id_front = models.ImageField(upload_to='id_images/')
    id_back = models.ImageField(upload_to='id_images/')
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Perfil de {self.user.username}"
