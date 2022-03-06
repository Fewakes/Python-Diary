"""Defines url patterns for users."""

from django.conf.urls import include, url
from django.contrib.auth import login
from django.contrib.auth import views as auth_views



from . import views

app_name = 'users'
urlpatterns = [
    # Login page.
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),

    # Logout page.
    url(r'^logout/$', views.logout_view, name='logout'),

    # Registration page.
    url(r'^register/$', views.register, name='register'),
]