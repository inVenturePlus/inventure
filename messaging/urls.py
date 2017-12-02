from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
import views
from django.conf.urls import include, url

app_name = 'messaging'

urlpatterns = [
    # url(r'^inbox/$', views.inbox, name='messages_inbox'),
    # url(r'^sent/$', views.outbox, name='messages_outbox'),
    # url(r'^compose/$', views.compose, name='messages_compose'),
    # url(r'^compose/(?P<recipient>[\w.@+-]+)/$', views.compose, name='messages_compose_to'),
    # url(r'^reply/(?P<message_id>[\d]+)/$', views.reply, name='messages_reply'),
    # url(r'^view/(?P<message_id>[\d]+)/$', views.view, name='messages_detail'),
    # url(r'^delete/(?P<message_id>[\d]+)/$', views.delete, name='messages_delete'),
    # url(r'^trash/$', trash, name='messages_trash'),
]

