from django.db import models

class UserDetail(models.Model):
    email = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=30)   