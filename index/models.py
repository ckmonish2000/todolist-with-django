from django.db import models

# Create your models here.


class buststops(models.Model):
    code=models.CharField(max_length=64)
    city=models.CharField(max_length=64)

    
    def __str__(self):
        return f"{self.code} {self.city}"


class bus(models.Model):
    origin=models.ForeignKey(buststops,on_delete=models.CASCADE,related_name="depart")
    destination=models.ForeignKey(buststops,on_delete=models.CASCADE,related_name="arrive")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} {self.destination} {self.duration}"



