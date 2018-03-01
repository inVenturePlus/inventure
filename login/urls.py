from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from login import views as login_views
from users import views as users_views
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import logout

from django.conf import settings
from django.conf.urls.static import static

app_name = 'login'

def dispatch_by_role(entrepreneur_view, vc_view):
    def get_view(request, **kwargs):
        if (is_entrepreneur(request.user)):
            return entrepreneur_view(request, **kwargs)
        else:
            return vc_view(request, **kwargs)
    return login_required(get_view)

def is_entrepreneur(user):
    return user.entrepreneur

urlpatterns = [

    url(r'^$', dispatch_by_role(login_views.EntrepreneurView, login_views.VCView), name='dashboard'),

    url(r'^create_user/$', login_views.CreateUser, name='create_user'),
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login/login.html'}, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^self/', include('users.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
