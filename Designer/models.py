from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_designerwork(models.Model):
     category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
     subcategory=models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
     material=models.ForeignKey(tbl_material, on_delete=models.CASCADE)
     color=models.ForeignKey(tbl_color, on_delete=models.CASCADE)
     designer=models.ForeignKey(tbl_designer, on_delete=models.CASCADE,null=True)
     work_details = models.CharField(max_length=50)
     designerwork_photo = models.FileField(upload_to='Assets/DesignerworkPhoto/')
     designerwork_rate =  models.IntegerField(default="0")
     designerwork_duration =  models.IntegerField(default="0")
     designer = models.ForeignKey(tbl_designer, on_delete=models.CASCADE,null=True)

class tbl_gallery(models.Model):
     gallery_file = models.FileField(upload_to='Assets/DesignerGallery/')
     designerwork_id=models.ForeignKey(tbl_designerwork, on_delete=models.CASCADE)
     gallery_caption=models.TextField(max_length=50)
