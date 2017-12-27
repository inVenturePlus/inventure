# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from custom_user.models import AbstractEmailUser
from django.conf import settings
from django.core.mail import send_mail
from fernet_fields import EncryptedCharField
from django_countries.fields import CountryField

from django.db import models

class VentureCapitalist(models.Model):
    company_name = models.CharField(max_length=150, default="")
    company_state = models.IntegerField(null=True)
    
    company_city = models.CharField(max_length=2)
    
    company_mission = comment = models.TextField(verbose_name="Mission statement of the company.", blank=True)
    company_fund_size = models.IntegerField(null=True)
    stages_interested = models.CharField(max_length=2)
    
    stages_avoid = models.CharField(max_length=2)
    locations_interested = models.CharField(max_length=2)
    locations_avoid = models.CharField(max_length=2)
    check_size = models.IntegerField(null=True)
    sector_interested = models.IntegerField(null=True)
    sector_avoid = models.IntegerField(null=True)
    previous_investments = models.TextField(verbose_name="Previous investments.", blank=True)
   
   
class Entrepreneur(models.Model):
    company_name = models.CharField(max_length=150, default="")
    company_location = models.IntegerField(null=True)
    
    company_city = models.CharField(max_length=2)
    
    company_mission = comment = models.TextFie 
    current_stage = models.CharField(max_length=2)
    
    locations_interested = models.CharField(max_length=2)
    check_size = models.IntegerField(null=True)
    sector = models.IntegerField(null=True)
    other = models.TextField(verbose_name="Previous investors, etc.", blank=True)
   
    
