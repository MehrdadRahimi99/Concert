from django.db import models

# Create your models here.
class consertmodel (models.Model):
    Name = models.CharField(max_length=100)
    SingerName = models.CharField(max_length=100)
    Length = models.IntegerField()
    
    def __str__(self):
        return self.SingerName
    
class locationmodel (models.Model):
    IdNumbers = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=500,default="تهران برج میلاد")
    Phone = models.CharField(max_length=11, null=True)
    Capacity = models.IntegerField()
    
    def __str__(self):
        return self.Name    

class timemodel(models.Model):
    concertmodel = models.ForeignKey("to=consertmodel", on_delete=models.PROTECT)
    locationmodel = models.ForeignKey("to=locationmodel", on_delete=models.PROTECT)
    startdatetime = models.DateTimeField()
    seats = models.IntegerField()