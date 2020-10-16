"""authorizator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from cas_server import views as casViews
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.decorators.debug import sensitive_post_parameters, sensitive_variables



urlpatterns = [
   path('authorizator/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
   path('authorizator/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
   url(r'^authorizator/cas/', include('cas_server.urls', namespace="cas_server")),

]
