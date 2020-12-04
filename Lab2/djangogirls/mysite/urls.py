"""mysite URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views
from blog import views as blog_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='blog/base.html'), name='logout'),
    path('password_change/',views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(template_name='registration/password_done.html'), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='registration/password_rdone.html'), name='password_reset_done'),
    path('reset/MQ/set-password/', views.PasswordResetDoneView.as_view(template_name='registration/password_set.html'), name='password_set'),
    path('signup/', blog_views.signup, name='signup'),
    url(r'^', include('django.contrib.auth.urls')),
]
