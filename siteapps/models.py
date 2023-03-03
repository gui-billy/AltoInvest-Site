from django.contrib.auth.models import User  # noqa: F401
from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=65, verbose_name=('name'))
    broker = models.CharField(max_length=65)
    account = models.IntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return self.name