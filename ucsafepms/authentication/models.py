from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
# class Role(models.Model):
#     id=models.AutoField(primary_key=True)
#     role_name=models.CharField(max_length=255)
#     title=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()
    
# class Users(models.Model):
#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField(max_length=255)
#     title=models.CharField(max_length=255)
#     role=models.ForeignKey(Role,on_delete=models.SET_NULL)
#     email=models.CharField(max_length=255)
#     username=models.CharField(max_length=255)
#     password=models.CharField(max_length=255)
#     profile_pict=models.CharField(max_length=255)
#     is_active=models.BooleanField(default=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

