from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField(max_length=50)
    hangout = models.CharField(max_length=50)
    feedback = models.IntegerField()
    def  __unicode__(self):
        return self.user.username
    
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    hangout = models.URLField(blank=True)

class Invited(models.Model):
    user = models.ForeignKey(User)
    appointment = models.ForeignKey(Appointment)

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def  __unicode__(self):
        return self.name

class MenuElement(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu)
    order = models.IntegerField(default=100)
    text = models.CharField(max_length=50)
    link  = models.URLField()
    def  __unicode__(self):
        return self.text

