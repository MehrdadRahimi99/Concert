from django.db import models

# Create your models here.
class consertmodel (models.Model):
    Name = models.CharField(max_length=100)
    SingerName = models.CharField(max_length=100)
    Length = models.models.IntegerField()
    
    def __str__(self):
        return self.SingerName
    
class locationmodel (models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    Phone = models.CharField(max_length=11)
    Capacity = models.IntegerField()
    
    def __str__(self):
        return self.Name    
