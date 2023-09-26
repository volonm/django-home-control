from django.db import models

# Create your models here.


class Lamps(models.Model):
    ipaddressV4 = models.CharField(max_length=15)
    macaddress = models.CharField(max_length=12)


