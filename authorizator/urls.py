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
from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path(settings.SERVICE_PATH + 'login/', views.LoginView.as_view(), name='login'),
   path(settings.SERVICE_PATH + 'logout/', views.LogoutView.as_view(), name='logout'),
   path(settings.SERVICE_PATH + 'password_change/', views.PasswordChangeView.as_view(), name='password_change'),
   path(settings.SERVICE_PATH + 'password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
   path(settings.SERVICE_PATH + 'api/', include('pdc.authorization.urls')),
   path(settings.SERVICE_PATH + "api/", include('pdc.service.baseAPIUrls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
