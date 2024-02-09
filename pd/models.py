from django.db import models
from django.utils import timezone


class Prediction(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=10,default="")
    country = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    prediction = models.BooleanField(default=False)
    retinalScan = models.ImageField(upload_to='testimages')
    segmentedImage = models.ImageField(upload_to='segmented',default=None,null=True,blank=True)


class Feedback(models.Model):
    predction = models.ForeignKey(Prediction,on_delete=models.CASCADE)
    comments=models.CharField(default="",max_length=1000)
    isPredictionCorrect=models.BooleanField(default=True)

    

