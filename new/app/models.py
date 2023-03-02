from django.db import models
from datetime import datetime, date
# Create your models here.

class test(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=300)
    post_date = models.DateTimeField(auto_now_add=True)   
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.title