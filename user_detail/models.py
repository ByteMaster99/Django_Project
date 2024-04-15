from django.db import models
from datetime import datetime

# Create your models here.
class Registermodel(models.Model):
    firstname = models.CharField(max_length=300)
    lasttname = models.CharField(max_length=300)
    userid = models.CharField(max_length=300)
    password= models.IntegerField()
    mblenum= models.BigIntegerField()
    email = models.EmailField(max_length=400, null=True)



class address(models.Model):
    Line_1 = models.CharField(max_length=300)
    Line_2 = models.CharField(max_length=300)
    Pincode = models.CharField(max_length=300)
    State =models.CharField(max_length=300)
    District =models.CharField(max_length=300)
    City= models.CharField(max_length=300)
    created_by= models.IntegerField(null=False,blank=False)
    created_date = models.DateField(default=datetime.now)
    updated_by = models.IntegerField(null=False,blank=False)
    updated_date =models.DateField(default=datetime.now)
    status = models.SmallIntegerField(default=1)


class contact(models.Model):
    mobile =models.BigIntegerField()
    Email = models.CharField(max_length=300)
    Account = models.CharField(max_length=300)
    Benificary_Name = models.CharField(max_length=300)
    created_by= models.IntegerField(null=False,blank=False)
    created_date = models.DateField(default=datetime.now)
    updated_by = models.IntegerField(null=False,blank=False)
    updated_date =models.DateField(default=datetime.now)
    status = models.SmallIntegerField(default=1)

class Vendor(models.Model):
    Name = models.CharField(max_length=300)
    Code =models.CharField(max_length=300)
    GST = models.CharField(max_length=300)
    Pan=models.CharField(max_length=300)
    Branch =models.CharField(max_length=300)
    Address= models.ForeignKey(address,on_delete=models.SET_NULL,null=True)
    Contact= models.ForeignKey(contact,on_delete=models.SET_NULL,null=True)
    created_by= models.IntegerField(null=False,blank=False)
    created_date = models.DateField(default=datetime.now)
    updated_by = models.IntegerField(null=False,blank=False)
    updated_date =models.DateField(default=datetime.now)
    status = models.SmallIntegerField(default=1)



