from django.db import models

# Create your models here.
class ChennaiJobs(models.Model):
   date = models.DateField()
   company = models.CharField(max_length=100)
   title = models.CharField(max_length=100)
   eligibility = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   email = models.EmailField()
   phonenumber = models.BigIntegerField()

class HydJobs(models.Model):
   date = models.DateField()
   company = models.CharField(max_length=100)
   title = models.CharField(max_length=100)
   eligibility = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   email = models.EmailField()
   phonenumber = models.BigIntegerField()

class BangloreJobs(models.Model):
   date = models.DateField()
   company = models.CharField(max_length=100)
   title = models.CharField(max_length=100)
   eligibility = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   email = models.EmailField()
   phonenumber = models.BigIntegerField()