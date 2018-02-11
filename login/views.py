# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from users.forms import VentureCapitalForm, EntrepreneurForm
from users.models import VentureCapital, Entrepreneur
from login.models import *
from login.forms import *


from django.shortcuts import (get_object_or_404, get_list_or_404, render, render_to_response)
from django.http import (HttpResponseRedirect, HttpResponseForbidden)
from django.views import generic
import datetime
from django.template import (Context, RequestContext)
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import (authenticate, login, get_user_model)
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import (get_template, render_to_string)
from django.template import Context
from django.contrib.auth.models import BaseUserManager
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone


def EntrepreneurView(request):
    user = request.user
    user_info = UserForm(request.POST or None, instance=user)

    return render(request, "../../users/templates/users/dashboard.html", {"user" : user, "user_info": user_info})

def VCView(request):
    user = request.user
    user_info = UserForm(request.POST or None, instance=user)
    
    return render(request, "../../users/templates/users/dashboard.html", {"user" : user, "user_info": user_info})


def CreateUser(request):
    if request.POST:
        form = UserForm(request.POST)
        if (form.is_valid()):
            new_user = form.save(commit=False)
            new_user.save()
            if(new_user.entrepreneur):
                new_user.createE();
            else:
                new_user.createVC();

            # email confirmation
            return HttpResponseRedirect(reverse('login:dashboard'))
    else:
        form = UserForm()

    variables = {
        'form': form,
        'user': request.user
    }

    template = '../templates/login/create_user.html'

    return render(request, template, variables)
