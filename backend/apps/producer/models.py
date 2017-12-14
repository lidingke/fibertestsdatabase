import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.



class Instrument(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True)

    serialsnumber = models.CharField(max_length=30, null=False, blank=True, verbose_name="设备编号")
    instrumenttype = models.CharField(max_length=30, null=False, blank=True, verbose_name="设备型号")

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.instrumenttype+':'+self.serialsnumber

class Result(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True)

    corediameter = models.FloatField(default=0, verbose_name="纤芯直径")
    claddiameter = models.FloatField(default=0, verbose_name="包层直径")
    coreroundness = models.FloatField(default=0, verbose_name="纤芯不圆度")
    cladroundness = models.FloatField(default=0, verbose_name="包层不圆度")
    concentricity = models.FloatField(default=0, verbose_name="芯包同心度")

    fibertype = models.CharField(max_length=100,verbose_name="光纤型号")
    fiberLength = models.CharField(max_length=100,verbose_name="光纤长度")
    fiberNo = models.CharField(max_length=100,verbose_name="光纤盘号")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")

    # worker = Column(String(50), nullable=False)

    owner = models.ForeignKey(User, related_name='result', on_delete=models.CASCADE, verbose_name="测试人员")
    instrument = models.ForeignKey(Instrument, verbose_name="测试设备")

    class Meta:
        verbose_name = '测试结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}:{}".format(self.id,self.instrument,self.owner)
