from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
GENDER_CHCOICES = [
       ("MALE","male"),
       ("FEMALE", "female")
]
USER_TYPES =[
        ("CUSTOMERS","customers"),
        ("RIDERS","riders"),
        ("STAFFS","staffs"),
        ("ADMIN","admin")
]

class UserManger(BaseUserManager):
     
     def create_user(self, email,firstname, lastname,password=None,** extra_fields):
        if not email:
         raise TypeError('Email not provided')
        email = self.normalize_email(email)
        user =self.model(
        email  = email,
        firstname = firstname,
        lastname = lastname,
        **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
     
  
     def create_superuser(self, firstname, lastname, email, phone, password=None,**extra_fields):
         if password is None:
             raise TypeError("password should be set")
         user = self.create_user(email, password,lastname,firstname,phone,**extra_fields)
         user.is_superuser = True
         user.is_staff = True
         user.is_verified = True
         user.USER_TYPE = "ADMIN"
         user.save()

         return user

     


     

class CustomUser(AbstractBaseUser, PermissionsMixin):
       id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
       email = models.EmailField(max_length=255, unique=True)
       firstname = models.CharField(max_length=100)
       lastname = models.CharField(max_length=100)
       date_of_birth  = models.DateField(null=True,blank=True)
       phone = models.CharField(max_length=15, unique=True)
       gender = models.CharField(max_length=6,choices=GENDER_CHCOICES)
       nationality = models.CharField(max_length=50)
       address = models.TextField(null=True, blank=True)  # this makes it optional, textfield has an infinite max length
       is_verified = models.BooleanField(default=False)
       is_active = models.BooleanField(default=True)
       is_staff = models.BooleanField(default=False)
       user_type = models.CharField(max_length=10, choices=USER_TYPES, default=USER_TYPES[0][0])
       created_at = models.DateTimeField(auto_now_add=True)
       profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
       updated_at = models.DateTimeField(auto_now=True)
       USERNAME_FIELD ='email'
      
       REQUIRED_FIELDS = ['firstname', 'lastname', 'phone']
       objects = UserManger()

       def __str__(self):
            return f"{self.firstname} {self.lastname}"

       
       def tokens(self):
            refresh =RefreshToken.for_user(self)
            return{
                  'refresh': str(refresh),
                  'access': str(refresh.access_token),
            }
       

     #  def__str__(self):
      #    return f"{self.firstname}, {self.phone}"
       class Meta:
         db_table = "user"
      

       







# Create your models here.
