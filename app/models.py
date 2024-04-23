from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    experience = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    experience = models.CharField(max_length=255)

    def __str__(self):
        return self.name
