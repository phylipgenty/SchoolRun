import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schoolrun.settings")

app = Celery("schoolrun")
# Reads every CELERY_* setting, e.g. CELERY_BEAT_SCHEDULE.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
