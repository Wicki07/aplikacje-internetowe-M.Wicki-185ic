from django.urls import path

from . import views

urlpatterns = [
    path('worker1/', views.index, name='index'),
    path('worker2/', views.index2, name='index'),
]