from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.welcome, name = 'welcome'),
    url('^home/', views.home, name = 'home'),
    url('^accounts/profile/', views.user_profile, name = 'user_profile'),
    
]    