import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab7.settings')

celery_app = Celery('lab7')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()