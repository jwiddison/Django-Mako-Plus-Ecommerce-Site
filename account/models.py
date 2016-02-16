from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin


class User(AbstractUser):
    #Using TextFields here because its faster on PostgreSQL (instead of varchar)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip_code = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'User: %s (%s)' % (self.get_full_name(), self.username)

admin.site.register(User)
