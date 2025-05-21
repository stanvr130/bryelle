from django.db import models
#from user.models import CustomUser
from django.contrib.auth import get_user_model


import uuid

User = get_user_model()

class Business(models.Model):
      id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
      name = models.CharField(max_length=100)
      type = models.CharField(max_length=250)
      country = models.CharField(max_length=250)
      state = models.CharField(max_length=250)
      city = models.CharField(max_length=250)
      street = models.CharField(max_length=250)
      phone = models.CharField(max_length=250)
      logo = models.ImageField(upload_to="buisness/")
      owner = models.ForeignKey(User, on_delete=models.CASCADE)
      is_active = models.BooleanField(default=True)
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now=True)
      
      def __str__(self):
            return f'{self.name} by {self.owner.firstname} {self.owner.lastname}'





      


# Create your models here.
