from django.urls import path, include
from . import views


urlpatterns = [
      path('getuser/', views.getUser.as_view(), name='getuser'),
      path('isauthenticated/', views.isAuthenticated.as_view(), name='isauthenticated')
 ]
