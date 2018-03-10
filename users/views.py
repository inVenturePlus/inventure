# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from login.forms import UserForm
from login.models import MyCustomEmailUser
from users.forms import *
from users.models import *
from django.shortcuts import (get_object_or_404, get_list_or_404, render, render_to_response)

def Questionaire(request):
    user = request.user
    if(user.entrepreneur == 2):
        user_answers = get_object_or_404(Entrepreneur, pk=request.user.pk)
        form =  EntrepreneurForm(request.POST or None, instance=user_answers)
    else:
        user_answers = get_object_or_404(VentureCapital, pk=request.user.pk)
        form = VentureCapitalForm(request.POST or None, instance=user_answers)

    return render(request, "../../users/templates/users/questions.html", {"user" : user, "user_answers": user_answers, "user_form": form})

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

def GenerateMatches(request):
    user = request.user
    if request.method == 'POST':
        if(user.entrepreneur == 2):
            form =  EntrepreneurForm(request.POST)
            form.save()
            MakeMatchInDatabaseE(user.pk)
        else:
            form =  VentureCapitalForm(request.POST)
            form.save()
            MakeMatchInDatabaseV(user.pk)
    else:
        if(user.entrepreneur == 2):
            form =  EntrepreneurForm()
        else:
            form =  VentureCapitalForm()
    # company_name = form.cleaned_data['company_name']

# Generates a row @ matches database w/ match scores.
def MakeMatchInDatabaseE(e_id):
    all_v = VentureCapital.objects.all()
    # The `iterator()` method ensures only a few rows are fetched from
    # the database at a time, saving memory.
    for v in all_v.iterator():
        score = AlexMatchAlgo(e_id, v.pk)
        entrep = Entrepreneur.objects.get(pk=e_id)
        venture = VentureCapital.objects.get(pk=v.pk)
        Matches(entrepreneur=entrep, venturecapital=venture, match_score=score)
