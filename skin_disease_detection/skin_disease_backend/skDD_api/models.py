from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Profile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Making email unique
    phonenumber = models.CharField(max_length=16,null=True, blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class DataHistory(models.Model):
    history = models.CharField(max_length=70)
    image = models.ImageField(upload_to='data_history_images/')
    diseasename = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # New line

    def __str__(self):
        return f"Data History for {self.email}"