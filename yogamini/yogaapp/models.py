from django.db import models
import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Name', unique=True)
    lastname = models.CharField(max_length=50, verbose_name='Surname')
    email = models.EmailField(verbose_name='email', unique=True)
    address = models.CharField(max_length=50,)
    phonenum = models.BigIntegerField(verbose_name='Phone Number')
    date = models.DateField(verbose_name='date', default=datetime.date.today)
    time = models.TimeField(verbose_name='time', default=datetime.time(0, 0))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)  # Make it nullable for now

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = 'yoga_mini'
        unique_together = ['date', 'time']

