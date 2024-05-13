from django.db import models

# Create your models here.
from django.db import models
from Admin.models import *
# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")

class tbl_designer(models.Model):
    designer_name=models.CharField(max_length=50)
    designer_gender=models.CharField(max_length=50)
    designer_contact=models.CharField(max_length=50)
    designer_email=models.CharField(max_length=50)
    designer_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    designer_photo = models.FileField(upload_to='Assets/DesignerPhoto/')
    designer_proof = models.FileField(upload_to='Assets/DesignerProof/')
    designer_status = models.IntegerField(default="0")


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    designer_from = models.ForeignKey(tbl_designer,on_delete=models.CASCADE,related_name="designer_from",null=True)
    designer_to = models.ForeignKey(tbl_designer,on_delete=models.CASCADE,related_name="designer_to",null=True)