# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from login.forms import UserForm
from login.models import MyCustomEmailUser
from users.forms import *
from users.models import *

def Questionaire(request):
    user = request.user
    try:
        if(user.entrepreneur):
            user_answers = get_object_or_404(Entrepreneur, pk=request.user.pk)
            form =  EntrepreneurForm(request.POST or None, instance=entrepreneur)
        else:
            user_answers = get_object_or_404(VentureCapital, pk=request.user.pk)
            form = VentureCapitalForm(request.POST or None, instance=vc)
    except:
        if(user.entrepreneur):
            user.createE()
        else:
            user.createVC()
    user_info = UserForm(request.POST or None, instance=user)

    return render(request, "../../users/templates/users/questions.html", {"user" : user, "user_answers": user_answers, "user_form": form, "user_info": user_info})

def MatchResults(request):
    user = request.user
    try:
        if(user.entrepreneur):
            user_answers = get_object_or_404(Entrepreneur, pk=request.user.pk)
            form =  EntrepreneurForm(request.POST or None, instance=entrepreneur)
        else:
            user_answers = get_object_or_404(VentureCapital, pk=request.user.pk)
            form = VentureCapitalForm(request.POST or None, instance=vc)
    except:
        if(user.entrepreneur):
            user.createE()
        else:
            user.createVC()
    user_info = UserForm(request.POST or None, instance=user)

    return render(request, "../../users/templates/users/questions.html", {"user" : user, "user_answers": user_answers, "user_form": form, "user_info": user_info})
