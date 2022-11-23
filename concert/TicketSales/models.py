from django.db import models

# Create your models here.


class consertmodel (models.Model):
    Name = models.CharField(max_length=100)
    SingerName = models.CharField(max_length=100)
    Length = models.IntegerField()
<<<<<<< HEAD
=======
    test = models.CharField(max_length=10, null=True)
>>>>>>> develop
    
    def __str__(self):
        return self.SingerName


class locationmodel (models.Model):
    IdNumbers = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=500, default="تهران برج میلاد")
    Phone = models.CharField(max_length=11, null=True)
    Capacity = models.IntegerField()

    def __str__(self):
        return self.Name


class timemodel(models.Model):
    ConcertModel = models.ForeignKey(to=consertmodel, on_delete=models.PROTECT)
    LocationModel = models.ForeignKey(to=locationmodel, on_delete=models.PROTECT)
    StartDateTime = models.DateTimeField()
    Seats = models.IntegerField()

    Start = 1
    End = 2
    Cancle = 3
    Sales = 4
    status_choices = (("Start", "فروش بلیط شروع شده است"),
                      ("End", "فروش بلیط تمام شده است"),
                      ("Cancle", "این سانس کنسل شده است"),
                      ("Sales", "در حال فروش بلیط"))
    status = models.IntegerField(choices=status_choices)

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime,
                                                              self.ConcertModel.Name,
                                                              self.LocationModel.name)
