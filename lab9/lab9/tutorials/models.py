from django.db import models
from django.utils import timezone

class Tutorial(models.Model):
    marka = models.CharField(max_length=70, blank=False, default='')
    model = models.CharField(max_length=200,blank=False, default='')
    rejestracja = models.CharField(max_length=70, blank=False, default='')
    data_publikacji = models.DateField(blank=True, default=timezone.now)