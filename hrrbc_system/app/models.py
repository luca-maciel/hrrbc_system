from django.db import models

# Create your models here.

# class Patient(models.Model):
#     reg_hospitalar = models.CharField(max_length=20, unique=True)
#     name = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=11, unique=True)
#     rg = models.CharField(max_length=10, unique=True)
#     birth_date = models.DateField()
#     state = models.CharField(max_length=2)
#     city = models.CharField(max_length=100)
#     unity = models.CharField(max_length=100)
#     bed = models.CharField(max_length=10)
#     admission_date = models.DateField()
#     discharge_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f"{self.name} - {self.reg_hospitalar}"

# class Escort(models.Model):
#     name = models.CharField(max_length=100)
#     cpf = models.CharField(max_length=11, unique=True)
#     rg = models.CharField(max_length=10, unique=True)
#     phone = models.CharField(max_length=15)
#     state = models.CharField(max_length=2)
#     city = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)