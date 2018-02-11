# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import MyCustomEmailUser


class MyCustomEmailUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    pass

# Register your models here.
admin.site.register(MyCustomEmailUser, MyCustomEmailUserAdmin)