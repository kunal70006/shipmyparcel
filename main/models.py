from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Tracker(models.Model):
    tracking_no = models.CharField(max_length = 20) #smp12345678
    awb_no = models.TextField(max_length = 100)
    delivery_server = models.CharField(max_length = 254)
    
    def __str__(self):
        return self.tracking_no


