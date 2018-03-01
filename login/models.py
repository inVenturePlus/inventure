# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from custom_user.models import AbstractEmailUser
from users.models import VentureCapital, Entrepreneur
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyCustomEmailUser(AbstractEmailUser):
    company_name = models.CharField(max_length=255)
    entrepreneur = models.IntegerField(null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    role = models.CharField(max_length=255)
    objects = MyUserManager()

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
