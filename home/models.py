from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
    
class Enhance(models.Model):
    input_file = models.FileField(upload_to="inp/",max_length=250, null=True, default=None)
    ai_model = models.CharField(max_length=122)
    # output_path = models.TextField()
    ai_precision = models.CharField(max_length=122)
    in_resolution = models.IntegerField()
    interpolation = models.CharField(max_length=122)
    img_output = models.CharField(max_length=122)
    vid_output = models.CharField(max_length=122)
    date = models.DateField()