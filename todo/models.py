from django.db import models

# Create your models here.
class todo(models.Model):
    item=models.CharField(max_length=250)
    des=models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.item} "