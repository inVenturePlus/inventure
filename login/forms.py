from django import forms
from django.forms import ModelForm
from login.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.forms import SetPasswordForm
from django.forms.widgets import RadioSelect
from django.core.files.images import get_image_dimensions

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyCustomEmailUser
        exclude = ['date_joined', 'created_date', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'is_staff', 'is_active']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        ACCOUNT_TYPE = ((1, "Venture Capitalist"), (2, "Entrepreneur"))

        self.fields['entrepreneur'] = forms.ChoiceField(widget=forms.RadioSelect, choices=ACCOUNT_TYPE)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password does not match"
            )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
