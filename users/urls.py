from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from users import views as user_views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    url(r'^questionaire/$', user_views.Questionaire, name='questions'),
    url(r'^matches/$', user_views.MatchResults, name='matches'),
    url(r'^avatar/', include('avatar.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
