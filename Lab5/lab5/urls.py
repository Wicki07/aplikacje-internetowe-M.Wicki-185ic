from django.urls import path
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.zajecia, name='zajecia'),
    path('scrap/', views.szukaj, name="scrap"),
    path('xpath/', views.xml, name="xpath"),
]