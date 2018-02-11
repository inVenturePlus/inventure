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
        exclude = ['date_joined', 'created_date', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'employment_type', 'salary_type', 'assigned_to', 'is_staff', 'is_active']
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        ACCOUNT_TYPE = ((1, "Venture Capitalist"), (2, "Entrepreneur"))
        
        self.fields['entrepreneur'] = forms.ChoiceField( widget=RadioSelect(), choices=ACCOUNT_TYPE)
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password does not match"
            )
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar
        
        