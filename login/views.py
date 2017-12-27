# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def create_user(request):
    return render(request, '../templates/login/create_user.html', {})
