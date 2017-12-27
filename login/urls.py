from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
import views
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import logout

from django.conf import settings
from django.conf.urls.static import static

app_name = 'login'

urlpatterns = [
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
   
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
