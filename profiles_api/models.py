from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""


    def create_user(self, email, name, password=None):
        """Create a new user profiles"""
        if not email:
            raise valueError('User must have an email address.')     

        email = self.normalize_email(email) #Converting to small casing the second part of the mail
        user = self.model(email=email, name=name)  #Create a new model and save email and name  
        user.set_password(password) #Django provides this cryptic password technique to hash password
        user.save(using=self._db)# Django can support multiple databases , and the standard procedure is above one

        return user

    def create_super_user(self, email, name, password):
        """Create a new super user profiles"""

        user = self.create_user(email,name.password)
        user.is_super_user(True) # comes from 'PermissionsMixin'
        user.is_staff(True)
        user.save(using=self._db)

        return user



class UserProfile (AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    """Mandatory Fields"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name


    def __str__(self):
        """Returns string representation of user"""        
        return self.email
