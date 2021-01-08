from django.conf.urls import url, include 
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    url(r'^', include('tutorials.urls')),
]