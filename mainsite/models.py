from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=20,null=False)
    enabled=models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class playinfo(models.Model):
    playno=models.CharField(max_length=20)
    playname=models.CharField(max_length=20)
    class1=models.IntegerField(max_length=5)
    xiangmu=models.CharField(max_length=5)
    mingci=models.CharField(max_length=5,blank=True)

    def __unicode__(self):
        return self.playno

class classinfo(models.Model):
    class1=models.CharField(max_length=10)
    score=models.CharField(max_length=20)

    def __unicode__(self):
        return self.class1
