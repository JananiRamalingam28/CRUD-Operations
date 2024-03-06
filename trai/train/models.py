from django.db import models

# Create your models here.
class d(models.Model):
    FN=models.CharField(max_length=20,default="")
    LN=models.CharField(max_length=20,default="")
    user=models.CharField(max_length=15,default="")
    email=models.CharField(max_length=25,default="")
    contact=models.IntegerField(max_length=10,default="")
    password=models.CharField(max_length=15,default="")
    cpass=models.CharField(max_length=15,default="")