from django.db import models

# Create your models here.


class concertmodel (models.Model):
    
    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"
        
    Name = models.CharField(max_length=100, verbose_name ="نام کنسرت")
    SingerName = models.CharField(max_length=100, verbose_name ="خواننده")
    Length = models.IntegerField(verbose_name =" مدت زمان")
    Poster = models.ImageField(upload_to = "concertimages/", null=True, verbose_name = "‍‍‍‍‍‍‍‍‍پوستر")
    
    def __str__(self):
        return self.SingerName


class locationmodel (models.Model):
    
    class Meta:
        verbose_name = "مکان"
        verbose_name_plural = "مکان"
    
    IdNumbers = models.IntegerField(primary_key=True , verbose_name = "کد محل")
    Name = models.CharField(max_length=100, verbose_name = "نام")
    Address = models.CharField(max_length=500, default="تهران برج میلاد", verbose_name = "آدرس")
    Phone = models.CharField(max_length=11, null=True, verbose_name = "تلفن")
    Capacity = models.IntegerField(verbose_name = "ظرفیت")

    def __str__(self):
        return self.Name


class timemodel(models.Model):
    
    class Meta:
        verbose_name = "زمان"
        verbose_name_plural = "زمان"
        
    ConcertModel = models.ForeignKey(to=concertmodel, on_delete=models.PROTECT, verbose_name ="کنسرت")
    LocationModel = models.ForeignKey(to=locationmodel, on_delete=models.PROTECT, verbose_name ="مکان")
    StartDateTime = models.DateTimeField(verbose_name ="تایم شروع")
    Seats = models.IntegerField(verbose_name ="صندلی")

    Start = 1
    End = 2
    Cancle = 3
    Sales = 4
    status_choices = (("Start", "فروش بلیط شروع شده است"),
                      ("End", "فروش بلیط تمام شده است"),
                      ("Cancle", "این سانس کنسل شده است"),
                      ("Sales", "در حال فروش بلیط"))
    status = models.IntegerField(choices=status_choices, verbose_name ="وضعیت")

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime,
                                                              self.ConcertModel.Name,
                                                              self.LocationModel.name)


class profilemodel(models.Model):
    
    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل"
    
    Name = models.CharField(max_length=100, verbose_name ="نام")
    Family = models.CharField(max_length=100, verbose_name ="نام خانوادگی")
    ProfiletImage = models.ImageField(upload_to = "profileimages/", verbose_name ="عکس پروفایل")
    Man = 1
    Woman = 2
    status_choises = (("Man","مرد"), ("Woman","زن"))
    Gender = models.IntegerField(choices= status_choises, verbose_name ="جنسیت")
    
    def __str__(self):
        return "fullname: {} {}".format(self.Name, self.Family)
    
    
class ticketmodel(models.Model):
   
    class Meta: 
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط"
    
    ProfileModel = models.ForeignKey("profilemodel", on_delete=models.PROTECT, verbose_name ="پروفایل")
    TimeModel = models.ForeignKey("timemodel", on_delete=models.PROTECT, verbose_name ="زمان")
    Name = models.CharField(max_length=100, verbose_name ="نام")
    Price = models.IntegerField(verbose_name ="قیمت")
    TicketImage = models.ImageField(upload_to = "ticketimages/", verbose_name = "تصویر")
    
    def __str__(self):
        return "ticketinfo: profile: {} concertinfo: {}".format(timemodel.__str__)