from django.contrib.auth.models import AbstractUser
from django.db import models


class CoreUser(AbstractUser):
    # add your extra fields here
    contact_number = models.IntegerField(null=True, blank=True)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.email
