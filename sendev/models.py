from django.db import models

# Create your models here.

class contact(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)
    age=models.IntegerField()
    location=models.CharField(max_length=50)
    icon = models.ImageField(upload_to='uploadslogo',null=True) 
class users(models.Model):
    nom=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    motDePasseUser=models.Field(max_length=200)
