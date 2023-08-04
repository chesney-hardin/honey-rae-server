from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=155)

    # this is called a property decorator
    @property
    def full_name(self):
        # use an f string 
        return f'{self.user.first_name} {self.user.last_name}'
    