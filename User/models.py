from django.db import models
from Guest.models import *

# Create your models here.

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

#user feedback
    
class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
    designer = models.ForeignKey(tbl_designer, on_delete=models.CASCADE,null=True)

class tbl_review(models.Model):
    review_name=models.CharField(max_length=200)
    Rating_details=models.IntegerField(default="0")
    Comment_details=models.CharField(max_length=200)