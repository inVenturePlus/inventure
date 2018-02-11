# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from custom_user.models import AbstractEmailUser
from users.models import VentureCapital, Entrepreneur

class MyCustomEmailUser(AbstractEmailUser):
    
    company_name = models.CharField(max_length=255)
    entrepreneur = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    role = models.CharField(max_length=255)
    avatar = models.ImageField()
    
    def createE(self):
        entrepreneur = Entrepreneur(pk=self.pk)
        entrepreneur.company_name = self.company_name
        entrepreneur.save()
        
    def createVC(self):
        vc = VentureCapital(pk=self.pk)
        vc.company_name = self.company_name
        vc.save()    
    
    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.company_name)
    
    def __unicode__(self):
        return "%s" % (self.company_name)
    
    class Meta:
        db_table = u'users'
        