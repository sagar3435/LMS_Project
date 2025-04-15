from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AdminManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Admins must have an email address")
        admin = self.model(email=self.normalize_email(email))
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

class Admin(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = AdminManager()

    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title
