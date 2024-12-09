from django.db import models

# Create your models here.
class User(models.Model):
    cid=models.CharField(max_length=20,null=True,blank=True)
    cname=models.CharField(max_length=220)
    cqty=models.CharField(max_length=220,null=True,blank=True)
    cprice=models.CharField(max_length=220,null=True,blank=True)

